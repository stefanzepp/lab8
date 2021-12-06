import nltk
# nltk.download()


def log(msg, mode='log'):
    filename = 'result.txt' if mode == 'res' else 'logger.txt'
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{msg}\n')


def clear_files():
    open('logger.txt', 'w').close()
    open('result.txt', 'w').close()


if __name__ == "__main__":
    clear_files()
    with open('text', 'r', encoding='utf-8') as file:
        data = file.read()
    sentences = nltk.sent_tokenize(data)
    sentences_extra = []
    for sentence in sentences:
        sentences_extra += sentence.split('\n')
    sentences_extra = [sentence for sentence in sentences_extra if sentence]

    tok = lambda token: token[1][:2]
    filt = lambda token: True if token in ['NN', 'VB'] else False
    cond_format = lambda token: ''.join(token)
    cond = lambda token: True if 'NNVBNN' in token else False

    for sent in sentences_extra:
        log(f'Sentence: {sent}')
        tokens = nltk.pos_tag(nltk.word_tokenize(sent))
        log(f'Tokens: {tokens}')
        tokens = [tok(token) for token in tokens]
        log(f'Toks of tokens: {tokens}')
        tokens = [token for token in tokens if filt(token)]
        log(f'Needed toks: {tokens}')
        tokens = cond_format(tokens)
        log(f'Condition format toks: {tokens}')
        if cond(tokens):
            log(sent, 'res')
            log('Valid')
        else:
            log('Skipped')
