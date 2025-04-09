## 📜 Opis skryptów w projekcie AI

### `MergeFolder.py`
Skrypt służy do:
- Iteracji przez foldery `CPJ1` do `CPJ17`.
- Wyszukiwania plików `.bmp` w każdym folderze.
- Kopiowania ich do folderu `Merged`.
- Nadawania nowej nazwy każdemu plikowi w formacie: `CPJ{numer_folderu}_{oryginalna_nazwa}.bmp`.

### `main.py`
Skrypt odpowiedzialny za:
- Wczytanie plików `.bmp` z folderu `Merged`.
- Binarizację każdego obrazu (zmiana pikseli na czarne lub białe według progu 45).
- Zapisanie przetworzonych obrazów do folderu `dataset_binarized2`.

### `script.py`
Służy do:
- Przemianowania wszystkich plików `.bmp` w folderze `DatasetMerged`.
- Zmienia nazwy na ustandaryzowany format: `plikMERGED{n}.bmp`, gdzie `n` to numer porządkowy.

### `scrpit2.py`
Zadaniem skryptu jest:
- Wczytanie każdego pliku `.bmp` z folderu `dataset_binarized`.
- Przycięcie obrazu z góry i dołu (usunięcie po 30 pikseli).
- Zapisanie nowego przyciętego obrazu z prefiksem `cropped_`.

### TEST.R
Zawiera:
- Funkcje do wczytywania obrazów i odpowiadających im masek z dwóch folderów.
- Możliwość wizualizacji wybranego obrazu i jego maski obok siebie.
- Używa bibliotek `magick`, `grid`, `gridExtra` do wyświetlania grafiki.
- Umożliwia użytkownikowi wybór konkretnego indeksu obrazu do wyświetlenia.

