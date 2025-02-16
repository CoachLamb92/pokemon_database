# pokemon_terminal
**A portfolio piece highlighting various programming concepts**

The following is by no means an exhaustive list, it is just whichever chaotic way my mind was working at time of writing

# To-do list:
## Pressing:
- Create and test basic battlestate passing competing pokemon in as args (args will eventually be refactored into player and wild pokemon or rival trainer)
- Make battlestate useable in terminal
- Randomise enemy pokemon's moves (would love to implement an algorithm for this, but much much later)

## General:
- Add documentation
- Requirements file
- Use api requests to gather information about Pokemon and Moves (check API requests using insomnia)
- Create a database, add pokemon table and update it with data from the api requests
- Add move table and update it with data from the api requests
- Link tables to determine which moves a pokemon can learn
- Catch pokemon to add to trainer belt
- Catch pokemon to add to box once belt is full
- Heal pokemon with command (pokecenter)
- Partially heal pokemon with command (potion)
- Add typing effects using a type chart
- Crit chance attribute added to move class
- Create basic damage formula (including STAB and strengths/weaknesses and crit chance)
- Add pokemon status (test effects first)
- Heal pokemon status with command (full heal)
- Heal specific pokemon status with command (paralyse heal, burn heal, ice heal, awakening, antidote)
- Add status inflicting moves (including chance of effect)
- Add buff and debuff moves and effects (start with accuracy)
- Turn counter in battle
- Switching pokemon in battle
- Healing during battle (status and hitpoints)
- Look into pytest.fixture(scope=function) for testing

## Stretch:
- Create a bag
- implement item usage
- Create a pokedex
- Limit box size and add many boxes
- Text-based exploring (Ex: You are in viridian city, what would you like to do? Your options are: ...)
- ASCII art towns and routes (no moving character, just a visual representation of the area)
- ASCII art towns and routes with controllable character (static screen, no overworld)
- ASCII art towns and routes with controllable character (moving screen)

## Completed:
- ~~Basic Pokemon class implemented and tested~~ (still tons to add)
- ~~Basic Move class implemented and tested~~(ditto above <- pardon the pokemon pun)
- ~~Data file created~~ (just some pokemon and moves examples to be used in testing runs)
- ~~Figure out how to beautify the readme~~ Behold it in all it's glory
