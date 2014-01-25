## Relational Algebra Exercises Core Set (CoreEx-RA)

Q1. Find all pizzas eaten by at least one female over the age of 20. 

~~~
\project_{pizza} (
  (
    (\project_{name} \select_{gender='female'} Person)
      \intersect
    (\project_{name} \select_{age>20} Person)
  \join Eats)
)
~~~

Correct.

Also tried:

~~~
\project_{pizza} (
  \project_{name} \select_{gender='female' AND age>20} Person \join Eats
);
~~~

In symbols:

    π_{pizza} σ_{gender='female' ∧ age>20) (Person) ⨝ Eats

Q2. Find the names of all females who eat at least one pizza served by Straw Hat. (Note: The pizza need not be eaten at Straw Hat.)

~~~
\project_{name} (
  \project_{pizza, name} (
    ((\project_{name} \select_{gender='female'} Person)
    \join Eats))
  \join \project_{pizza} \select_{pizzeria='Straw Hat'} Serves)
~~~

Correct.

Also tried:

~~~
\project_{name} (
  \select_{gender='female' AND pizzeria='Straw Hat'} (
    Person \join Eats \join Serves
  )
);
~~~

In symbols:

    π_{name} σ_{gender='female' ∧ pizzeria='Straw Hat'} (Person ⨝ Eats ⨝ Serves)

Q3. Find all pizzerias that serve at least one pizza for less than $10 that either Amy or Fay (or both) eat. 

~~~
\project_{pizzeria} (
    \project_{pizza,pizzeria} \select_{price<10} Serves
    \join
    \project_{pizza} \select_{name='Amy' OR name='Fay'} Eats
)
~~~

Correct.

Q4. Find all pizzerias that serve at least one pizza for less than $10 that both Amy and Fay eat. 

~~~
\project_{pizzeria} (
    \project_{pizza,pizzeria} \select_{price<10} Serves
    \join
    (
      (\project_{pizza} \select_{name='Amy'} Eats)
      \intersect
      (\project_{pizza} \select_{name='Fay'} Eats)
    )
)
~~~

Correct.

Q5. Find the names of all people who eat at least one pizza served by Dominos but who do not frequent Dominos. 

First find people who eat pizzas served by Dominos.

~~~
\project_{name} (
  \rename_{name, pizzaEats} \project_{name, pizza} Eats 
  \join_{pizzaEats=pizzaServes}
  (\rename_{pizzaServes} \project_{pizza} \select_{pizzeria='Dominos'} Serves)
)
~~~

Then subtract (`\diff`) people who frequent Dominos: `\project_{name} \select_{pizzeria='Dominos'} Frequents`.

~~~
\project_{name} (
  \rename_{name, pizzaEats} \project_{name, pizza} Eats 
  \join_{pizzaEats=pizzaServes}
  (\rename_{pizzaServes} \project_{pizza} \select_{pizzeria='Dominos'} Serves)
)
\diff (\project_{name} \select_{pizzeria='Dominos'} Frequents)
~~~

Correct.