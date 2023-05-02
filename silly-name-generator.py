from random import choice
from random import random

first = ('Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn',    'Liam', 'Noah', 'William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas', 'Mason', 'Logan',    'Alexander', 'Ethan', 'Jacob', 'Michael', 'Daniel', 'Henry', 'Jackson', 'Sebastian', 'Aiden', 'Matthew',    'Abigail', 'Emily', 'Sofia', 'Avery', 'Ella', 'Scarlett', 'Grace', 'Chloe', 'Victoria', 'Riley',    'Mila', 'Layla', 'Lily', 'Nora', 'Zoe',
         'Stella', 'Violet', 'Claire', 'Hazel', 'Aurora',    'Natalie', 'Samantha', 'Maria', 'Lucy', 'Ruby', 'Eva', 'Sophie', 'Sadie', 'Luna', 'Piper',    'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Carter', 'Julian', 'Luke', 'Greyson', 'Jayden',    'Owen', 'Gabriel', 'Connor', 'Charles', 'Jaxon', 'Lincoln', 'Christopher', 'Isaiah', 'Andrew', 'Theodore',    'Joshua', 'Nicholas', 'Christian', 'Thomas', 'Aaron', 'Landon', 'Nathan', 'Jonathan', 'Nolan', 'Easton')

middle = (
    'Zephyrina', 'Quixley', 'Fendrel', 'Ysabelline', 'Xylander', 'Wolfsbane', 'Velvetina', 'Utheria',
    'Thistlewick', 'Sylvarius', 'Ravensara', 'Quizzabella', 'Primarosa', 'Oberonia', 'Nimrodel', 'Myrtille',
    'Lunaria', 'Kestrelia', 'Jaspertine', 'Isabellatrix', 'Hespera', 'Galadrielle', 'Fenwick', 'Elowen',
    'Drusander', 'Cymbeline', 'Bramblewood', 'Aurembiaix', 'Alaric', 'Eglantine', 'Iolanthe', 'Crispin',
    'Xanthippe', 'Tallulah', 'Serendipity', 'Peregrine', 'Meridian', 'Lysander', 'Horatio', 'Felicity',
    'Zinnia', 'Valerian', 'Theodosia', 'Sequoia', 'Rhapsody', 'Persephone', 'Morpheus', 'Lilith', 'Gwydion',
    'Endymion', 'Cassiopeia', 'Balthazar', 'Araminta', 'Zephyr', 'Vespertine', 'Thaddeus', 'Sylvester',
    'Rowena', 'Quetzal', 'Phineas', 'Magenta', 'Lucasta', 'Hypatia', 'Gideon', 'Fandango', 'Euphemia',
    'Cosmo', 'Boadicea', 'Andromeda', 'Ziggy', 'Viridian', 'Titania', 'Solstice', 'Rufus', 'Quest',
    'Philomena', 'Melisandre', 'Leopold', 'Ignatius', 'Hermione', 'Griselda', 'Fitzwilliam', 'Esmerelda',
    'Cleopatra', 'Benedict', 'Ambrosia', 'Wystan', 'Xenobia', 'Winter', 'Ulysses', 'Tiberius', 'Saskia',
    'Romulus', 'Quintessa', 'Ophelia', 'Narcissa', 'Marmaduke', 'Lazarus', 'Jezebel', 'Isolde', 'Huxley',
    'Guinevere', 'Fitzroy', 'Ezekiel', 'Circe', 'Beowulf', 'Aloysius'
)


last = (
    'Fintacor', 'Zelthorn', 'Brinmara', 'Quilthorpe', 'Mendaville', 'Glarinford', 'Vendalight', 'Strinweaver',
    'Crevaston', 'Tinthallow', 'Ferrowist', 'Chromagear', 'Drethcage', 'Vaneshadow', 'Flarowist', 'Strynewood',
    'Thistledark', 'Velvetmire', 'Whispfrost', 'Grimestone', 'Cobaltglen', 'Duskwhistle', 'Valthorne', 'Mistcreek',
    'Rivenbrook', 'Stormgarde', 'Glimmerveil', 'Nethermire', 'Shadewhisper', 'Frostgrove', 'Silentfen', 'Gloomcrag',
    'Galehollow', 'Emberstone', 'Cinderwood', 'Wraithcove', 'Phantomhollow', 'Shadowbriar', 'Ironhollow',
    'Goblinwatch', 'Tidewhisper', 'Ghosthollow', 'Ravencrest', 'Ebonmire', 'Doomspire', 'Balewind', 'Duskweaver',
    'Grimward', 'Nightsorrow', 'Thundermire', 'Dreadscar', 'Eclipsemourn', 'Umbralcross', 'Duskcloak', 'Woebringer',
    'Banespire', 'Darktide', 'Gloombane', 'Shadowthorn', 'Voidmourn', 'Cryptshadow', 'Sorrowfen', 'Gloomspire',
    'Rimehollow', 'Blightglen', 'Bramblefrost', 'Sablethorn', 'Moonshadow', 'Gravewhisper', 'Sorrowveil',
    'Abyssfen', 'Hauntgrove', 'Blackcrag', 'Nightscar', 'Chillgarde', 'Bleakmourn', 'Duskcrag', 'Griefhollow',
    'Deathgrove', 'Hollowcross', 'Wraithgarde', 'Doomwhisper', 'Gloomhollow', 'Felshroud', 'Ruinwatch',
    'Shadowgarde', 'Nethercrag', 'Doomhollow', 'Gravegarde', 'Hauntspire', 'Ebonfen', 'Balegrove', 'Shadowmire',
    'Umbragarde', 'Wraithspire', 'Frostscar', 'Nightwhisper'
)

if random() <= 0.5:
    print(f'{choice(first)} {choice(last)}')
else:
    print(f'{choice(first)} {choice(middle)} {choice(last)}')
