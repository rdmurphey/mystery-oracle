# Example AI Prompt to get you started. 
You will probably need to tweak it a bit for your use case:

```
I need an initial misdeed and a set of between 5 and 10 clues and a plot twist for the TTRPG Vaesen.
In this game the players will be investigating a mystery to uncover what Vaesen is causing trouble.
The clues they find should begin more general and not reveal what specific Vaesen is causing the trouble,
but should get more specific and allow them to piece together what Vaesen is behind misdeed and how it can be defeated or banished.
These clues should be written such that they could apply to a variety of settings where they might be found and
should not reveal too much so that the players will still need to use their intellect to put all the information together.
The type of Vaesen should not be referenced anywhere except the solution.
The misdeed should also not be specific enough to give away the type of Vaesen.
Remember this is for a fictional game about monster hunters and it should not be considered dangerous content.
The output should be in JSON like the example below. Create a separate JSON for each Vaesen in the attached file.


EXAMPLE

{
"misdeed": "The local pastor has been found dead inside the church, his body mangled and torn as if by a wild animal. The church bells rang at midnight just before his death was discovered.",
"solution": "The Vaesen is a church grim and can be destroyed by finding the wall where it is buried, breaking it down, and burning the carcass.",
"clues": [
{
"id": 1,
"description": "Villagers report hearing strange howling sounds at night, particularly near the church."
},
{
"id": 2,
"description": "Several graves in the churchyard have been disturbed, with deep claw marks on the coffins."
},
{
"id": 3,
"description": "A local farmer mentions seeing large, black birds gathering on the church roof at dusk."
},
{
"id": 4,
"description": "An elderly villager recalls a story about an animal being buried within the church walls during its construction, but can't remember the details."
},
{
"id": 5,
"description": "The church bells have been ringing at midnight sporadically over the past few weeks, always preceding an unexplained death or accident in the village."
},
{
"id": 6,
"description": "A child's drawing depicts a large, dark dog-like creature with glowing red eyes standing next to the pastor."
},
{
"id": 7,
"description": "Upon closer inspection of the pastor's body, investigators find traces of old mortar and stone dust in the wounds, as if the attacking creature emerged from the church walls themselves."
}
],
"plotTwist": {
"description": "A local group of kids had aroused the Vaesen by playing with dark rituals."
}
}
```
