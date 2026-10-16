1. Encapsulation means packaging it all together with methods that operate in that data instead of keeping them loose together; like, a product could keep name, price, and quantity as private attributes, and make methods like restock or sell, public. This action will protect the data from being modified incorrectly elsewhere in the program, like, sell can check for stock before subtracting, whereas a plain variable could've easily skipped this. Encapsulation, in summary, keeps product's data and behavior together.

2. Abstraction is hiding the irrelevant details of how something works behind, and only showing what's necessary. This makes the program easier to use and to modify, which makes revisions easier to be done since changes to the internal stuff doesn't affect how the program interact with the object

3. Inheritance allows for a general product class to serve as template for more specific products. Much like genetics, the subclasses inherits or gets common attributes and/or common methods. This makes it easier for the coder to not rewrite every time for a product type. But a subclass can add its own attribute, but it cannot touch the base class.

4. Polymorphism, from its root word, it morphs to allow different product subclasses to respond differently to the same method call. This lets the store loop through a single list of mixed product types and call the same method on each but letting each object handle things their own way.

Product
├── name, price, quantity
├── sell(qty)
└── displayInfo()
Perishable (inherits Product)
├── expirationDate
├── isExpired()
└── sell(qty) // overridden: checks isExpired() first
NonPerishable (inherits Product)
└── displayInfo() // overridden: shows different details

Reflection
In a sari-sari store system, encapsulation would be the most useful for both the buyer and the ownerr. It allows for grouping of related data so that it won't be a hassle to look for it, and it also adds a layer of safety since actions like selling or restocking can validate the data first instead of allowing for it to be changed instantly which can cause to incorrect data.
