import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bookepedia_project.settings')
import django
django.setup() 
from bookepedia_project import settings
from bookepedia.models import Genre, Book


def populate():
    genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']

    for genre_name in genres:
        genre = Genre.objects.get_or_create(name=genre_name)

    books = {
        'Action': [
            {
                'title': 'The Bourne Identity',
                'author': 'Robert Ludlum',
                'description': 'A gripping action thriller about an amnesiac man who discovers he is a highly trained assassin.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Die Hard',
                'author': 'Roderick Thorp',
                'description': 'A classic action-packed story of a New York City cop who takes on terrorists in a Los Angeles skyscraper.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Gunslinger',
                'author': 'Stephen King',
                'description': 'The first book in The Dark Tower series, blending elements of fantasy and western genres with action-packed scenes.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Adventure': [
            {
                'title': 'Treasure Island',
                'author': 'Robert Louis Stevenson',
                'description': 'A classic adventure novel about a young boy named Jim Hawkins and his journey to find buried treasure.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Adventures of Tom Sawyer',
                'author': 'Mark Twain',
                'description': 'Follow Tom Sawyer and his friend Huckleberry Finn as they embark on various adventures in the Mississippi River town of St. Petersburg.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'description': 'Join Bilbo Baggins, a hobbit who embarks on an unexpected adventure to reclaim the Lonely Mountain from the dragon Smaug.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Comedy': [
            {
                'title': 'The Hitchhiker\'s Guide to the Galaxy',
                'author': 'Douglas Adams',
                'description': 'A hilarious science fiction comedy about the misadventures of an ordinary human and his alien friend as they journey through space.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Good Omens',
                'author': 'Terry Pratchett, Neil Gaiman',
                'description': 'A satirical comedy about an angel and a demon who team up to prevent the apocalypse and save the world.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Bridget Jones\'s Diary',
                'author': 'Helen Fielding',
                'description': 'A humorous diary-style novel chronicling the romantic misadventures of Bridget Jones, a single woman in her thirties.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Drama': [
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'A powerful drama set in the racially charged atmosphere of the American South, exploring themes of morality and justice.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'A classic novel depicting the drama and decadence of the Jazz Age, with themes of love, wealth, and the American Dream.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Kite Runner',
                'author': 'Khaled Hosseini',
                'description': 'A gripping drama set in Afghanistan, following the friendship between two boys against the backdrop of political turmoil.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Horror': [
            {
                'title': 'Dracula',
                'author': 'Bram Stoker',
                'description': 'A chilling horror novel that introduced the iconic vampire Count Dracula and set the standard for vampire fiction.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Shining',
                'author': 'Stephen King',
                'description': 'A psychological horror novel about a writer who takes a job as the winter caretaker of a haunted hotel, with terrifying consequences.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Frankenstein',
                'author': 'Mary Shelley',
                'description': 'A classic horror tale about a scientist who creates a grotesque creature and unleashes chaos upon himself and society.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Romance': [
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A timeless romance novel about the complicated relationship between Elizabeth Bennet and Mr. Darcy in Georgian England.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Outlander',
                'author': 'Diana Gabaldon',
                'description': 'A sweeping romantic saga that combines elements of historical fiction, fantasy, and time travel, set in 18th-century Scotland.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'The Notebook',
                'author': 'Nicholas Sparks',
                'description': 'A heartwarming love story about a young couple who fall in love one summer but are torn apart by social class and war.',
                'cover': 'harry_potter.jpg'
            },
        ],
        'Sci-Fi': [
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'description': 'A science fiction epic set in a distant future where noble houses vie for control of the desert planet Arrakis, the only source of a valuable spice.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Foundation',
                'author': 'Isaac Asimov',
                'description': 'The first book in the Foundation series, exploring the rise and fall of a galactic empire in a future where psychohistory predicts the future of humanity.',
                'cover': 'harry_potter.jpg'
            },
            {
                'title': 'Ender\'s Game',
                'author': 'Orson Scott Card',
                'description': 'A science fiction novel about a young boy named Ender Wiggin who is recruited to attend a military training school in space to prepare for an alien invasion.',
                'cover': 'harry_potter.jpg'
            },
        ],
    }
    
    for genre_name, books in books.items():
        genre = Genre.objects.get(name=genre_name)

        for book_info in books:
            title = book_info['title']
            author = book_info['author']
            description = book_info['description']
            cover = os.path.join('book_covers', book_info['cover'])
            slug = f"{genre_name.lower().replace(' ', '-')}-{title.lower().replace(' ', '-')}"

            book = Book.objects.create(
                title=title,
                author=author,
                description=description,
                cover=cover,
                genre=genre,
                slug=slug
            )
            print(f'Book "{title}" created.')

if __name__=='__main__':
    print('Starting Bookepedia population script...') 
    populate()

