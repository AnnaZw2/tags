def test1_kwadrat(capsys):
    #given
    liczba=3
    #when
    kwadrat(liczba)
    result=capsys.readouterr()
    #then
    assert result.out=='9\n'
    assert result.err == ''

def test2_kwadrat(capsys):
    #given
    liczba=0
    #when
    kwadrat(liczba)
    result=capsys.readouterr()
    #then
    assert result.out=='0\n'
    assert result.err==''

