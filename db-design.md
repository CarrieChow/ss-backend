# Guidelines

* Please write your SQL code on a SQLFiddle, http://sqlfiddle.com/. Sample answer format: http://sqlfiddle.com/#!9/8f27bf/4
* When you are done, copy and send us the link to your Fiddle at engineering@sourcesage.co, with your name as the subject.
* Feel free to consult official MySQL documentation for syntax and implementation details to aid you.
* You can make some assumptions, as long as you write SQL comments/notes to explain your assumptions and decisions.
* If any requirements are unclear, feel free to drop us an email at engineering@sourcesage.co to clarify.

---

# Context

We would like to design a database to store and query available products, their contract details, and their quoted prices over time.

Each product has the following fields:

* an English name
* a short description (<200 words).

Some examples of products:

* "Palm oil", "used to manufacture sweeteners"
* "Fatty alcohol", "manufacture alcohol products"

Each contract has a number of details:

* packaging (e.g. bags, drums, cartons, etc.)
* name of shipping city (e.g. Shanghai, Kuala Lumpur, etc.)
* shipping terms (e.g. FOB, CIF, full list at https://en.wikipedia.org/wiki/Incoterms#Rules_for_any_mode_of_transport)

Each contract is linked to one product, and multiple prices.
Prices are tied to a contract and a date.

Some examples of contracts:

* "Palm oil, packed in cartons, delivered to Shanghai FOB, is priced at 1000 USD/MT on 12/12/2017."
* "Palm oil, packed in cartons, delivered to Shanghai FOB, is priced at 1080 USD/MT on 13/12/2017."
* "Palm oil, packed in cartons, delivered to Shanghai FOB, is priced at 1050 USD/MT on 14/12/2017."
* "Fatty alcohol, packed in drums, delivered to Hong Kong CIF, is priced at 120 USD/MT on 12/12/2017."

In this exercise, you may ignore the currency and unit for the prices.

---

# Questions

## Q1. Schema design

Design a suitable schema, SQL DDL is sufficient, no need for diagrams.

1. How many tables? what are the names and data types of each column?
2. Which columns are foreign keys? Between which tables? Is the relationship one-to-one, one-to-many, or many-to-many?

## Q2. Query writing

Write a MySQL query to:

1. count number of contracts for each product
2. count number of prices for each contract
3. average count of prices for each contract
4. average price of each product in past 30 days? in past 1 year?

## Q3. Optimization

How can you optimize the queries in Q2? Which columns would you _index_?

## Q4. Extension

If we need to support multiple names in different languages for products, how would you modify/extend the current schema to support:

1. Only english and chinese names?
2. Up to 10 languages for each product?
3. (BONUS) We want db to return the same product when English user searches for palm oil, Chinese user searches for 棕榈油 and/or Japanese user searches for パームオイル or パーム油. How can we achieve this?
