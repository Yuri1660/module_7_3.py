import string


class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()

                        line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))

                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result


with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write(
        "It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи! Text, text, text.")

finder = WordsFinder('test_file.txt')

all_words = finder.get_all_words()
print(all_words)

first_occurrence = finder.find('task')
print(first_occurrence)

word_count = finder.count('text')
print(word_count)