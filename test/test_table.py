from src import engine
from multiprocessing import Pool


def test_1():
    # Q1: Insert & delete bob
    with engine.begin() as conn:
        conn.execute("insert into user (name) values ('tony');")

        conn.execute("")

        result = conn.execute("select id, name from user order by id;")
        rows = result.fetchall()
        assert rows == [(1, "tony"), (2, "bob")], "Should insert bob record"

        conn.execute("")

        result = conn.execute("select id, name from user order by id;")
        rows = result.fetchall()
        assert rows == [(1, "tony")], "Should delete bob record"


def test_2():
    # Q2: Discard all the changes
    with engine.begin() as conn:
        for name in ["tony", "bob", "taro"]:
            conn.execute("insert into user (name) values ('%s');" % name)

        result = conn.execute("")
        row = result.first()
        assert row == (3, ), "Should create 3 records"

    with engine.begin() as conn:
        conn.execute("delete from user where id = 1;")
        conn.execute("update user set name = 'BOB' where name = 'bob';")
        conn.execute("insert into user (name) values ('hoge');")
        conn.execute("")

    with engine.begin() as conn:
        result = conn.execute("select name from user order by id;")
        rows = result.fetchall()
        assert rows == [("tony", ), ("bob",), ("taro", )], "Should discard all the changes"


def test_3():
    # Q3: Get tony's friends
    with engine.begin() as conn:
        conn.execute("insert into user (id, name) values (1, 'tony'), (2, 'bob'), (3, 'taro'), (4, 'ken'), (5, 'tanaka');")
        conn.execute("insert into contact (user_id, other_id) values (1, 2), (1, 3), (3, 4)")

    with engine.begin() as conn:
        result = conn.execute("")
        rows = result.fetchall()
        assert rows == [("bob", ), ("taro", )], "bob and taro should be tony's friend"

    with engine.begin() as conn:
        conn.execute("insert into contact (user_id, other_id) values (5, 1)")
        result = conn.execute("")
        rows = result.fetchall()
        assert rows == [("bob", ), ("taro", ), ("tanaka", )], "tanaka should be tony's friend too"


def test_4():
    # Q4: Get the student name who gets highest total scores across subjects
    # (user_id, score, subject)
    fixture = """
    (1, 7, 'math'), (1, 3, 'english'), (1, 8, 'physics'),
    (2, 6, 'math'), (2, 9, 'english'), (2, 7, 'physics'),
    (3, 3, 'math'), (3, 8, 'english'), (3, 6, 'physics')
    """
    engine.execute("insert into user (id, name) values (1, 'tony'), (2, 'bob'), (3, 'taro');")
    engine.execute("insert into score (user_id, score, subject) values %s ;" % fixture)

    result = engine.execute("")

    row = result.first()
    assert row == ("bob", 22), "bob should get the highest total 22 scores"


def run(i):
    # http://docs.sqlalchemy.org/en/latest/core/pooling.html#using-connection-pools-with-multiprocessing
    engine.dispose()  # for multiprocess

    with engine.begin() as conn:
        conn.execute("")  # wrtie SQL to fix dead lock
        if i % 2 == 0:
            # Send from tony account to bob account
            sender_id = 1
            receiver_id = 2
        else:
            # Send from bob account to tony account
            sender_id = 2
            receiver_id = 1
        conn.execute("update account set balance = balance - 20 where user_id = %s;" % sender_id)
        conn.execute("update account set balance = balance + 20 where user_id = %s;" % receiver_id)


def test_5():
    # Q5: tony and bob send 20 to each other 100 times concurrently
    with engine.begin() as conn:
        conn.execute("insert into user (id, name) values (1, 'tony'), (2, 'bob');")
        conn.execute("insert into account (user_id, balance) values (1, 100), (2, 200);")

    pool = Pool(processes=2)
    pool.map(run, range(100))

    engine.dispose()
    with engine.begin() as conn:
        result = conn.execute("")
        row = result.first()
        assert row == (300, ), "total balances should be 300"
