# Scaffold  
Scaffold is a Dungeons & Dragons/ classic Text-RPG inspired engine. It uses the code for the logic, artificial intelligence for the narration, and dungeon masters and world builders for storytelling.

# What does this project do/plan to do?

Scaffold is an incredibly flexible engine designed to create highly immersive and story driven campaigns and made to create entirely unique playthroughs where no two are the same. 

The engine handles the rules, mechanics and logic of the campaign, including, but not limited to; combat, dice rolls, relationships, and interactions. The world itself is handled through data files. 
Each campaigns player, enemies, characters, items, weapons, maps, locations, and other world attributes are stored in user-made JSON files and stored in specified directories. This file distinction 
makes it easier for world builders to express creativity without needing to know how to code. The narration is handled using AI, not to replace the creativity of the world builder, but to enhance the 
immersion of the campaign. Instead of simply reporting “Enemy does 5 damage.” The AI describes each action in a more engaging and personal way giving players the unique opportunity to interact with the 
world around them, while remaining true to the world and story created by the world builder. 

Since the engine’s mechanics and the world’s data are handled separately from the narration, the AI can focus solely on player interaction and story narration rather than managing game mechanics and 
memorizing world data. This allows smaller models to perform far beyond what might normally be expected of them and even perform beyond what other major campaign AI are capable of. Scaffold is capable of 
running with any LLM supported through Ollama, giving users the freedom and capability to choose a model that suits their needs. Meaning the only limitations to how powerful of a model is only determined 
by your personal hardware specs. By running the model locally, the player’s experience is not limited by API credits or subscriptions from major corporations, making Scaffold free and accessible for all 
users.

In other words, Scaffold is a unique 3 part engine system that makes full use of each component to allow for max customization and creativity. For players, Scaffold offers a unique campaign experience 
similar to that of an actual D&D, allowing for in depth world building, ensuring no two campaigns are the same. For world builders, it provides an interactive way to see their creations come to life with 
limitless possibilities. For all, Scaffold creates an engine, not limited by subscriptions, API keys, linear story, or confused AI models. 

# Fancy tech lingo:

Languages:

* Python (For mechanics and logic.)

Libraries:

* JSON
* Random
* Pathlib
* Ollama

Frameworks:

* TBD

# How to run:

This project is still in early development. Stay tuned for how to run!

# Update log:

* 9/23/2026: Made a good baseline for a fighting system.

* 9/22/2026: Created a suitable README that explains what this software is, why it was made, and how it runs.

* 9/21/2026: Minor bug fix in Entity class' isalive() function. Added more directories for future file organization.

* 9/20/2026: Tweaked the mechanics on how battles between Enemy and Player subclass should function.

* 9/18/2026: Began creating a solid base for Scaffold.


