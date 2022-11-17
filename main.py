import os


if __name__ == '__main__':
    wavlist = [f for f in os.listdir('wav') if f.endswith('wav')]
    print(wavlist)
    for wav in wavlist:
        print(wav)

        # wavargs = ' -Sright -v -p -o tzx\\' + wav + '.tzx wav\\' + wav
        wavargs = ' -Sright -v -tlow -Thigh -lshort -p -o tzx\\' + wav + '.tzx wav\\' + wav
        os.system(r'tzxwav' + wavargs)

        catargstxt = ' --text tzx\\' + wav + '.tzx > txt\\' + wav + '.txt'
        catargsbas = ' --basic tzx\\' + wav + '.tzx > bas\\' + wav + '.bas'
        catargspng = ' --screen --to png\\' + wav + '.png' + ' tzx\\' + wav + '.tzx'
        os.system(r'tzxcat' + catargstxt)
        os.system(r'tzxcat' + catargsbas)
        os.system(r'tzxcat' + catargspng)




