import csv
from models.word import Word_hy


class Importer_hy:

    @staticmethod
    def import_txt_hy(file_path):
        words = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if "," in line:
                    word, meaning = line.split(",", 1)
                    words.append(Word_hy(word, meaning))

        return words

    @staticmethod
    def import_csv_hy(file_path):
        words = []

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 2:
                    words.append(Word_hy(row[0], row[1]))

        return words