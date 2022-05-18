import os.path

from markov_gen.markov_gen import word_markovIt, ngram_markovIt


def read_file(filename: str) -> tuple[list, str]:
    with open(os.path.join(os.path.dirname(__file__), filename), mode="r") as f:
        txt = f.read().replace('\n', '')
    txt_list = txt.split()
    return txt_list, txt


def markov(corpus_name: str, size: int, use_word: bool):
    n_gram_order = 10
    txt_list, txt = read_file(corpus_name)
    generated = word_markovIt(txt_list, size) \
        if use_word else ngram_markovIt(txt, n_gram_order, size)
    return generated


def main():
    corpus_name = input('enter a corpus name: ')
    size = int(input('enter size: '))
    use_word = input('yes = word markov, no = order 10 n-gram: ').lower() in {'yes', 'y', '1', 'true'}
    print(markov(corpus_name, size, use_word))


if __name__ == '__main__':
    main()
