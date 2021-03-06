import os.path
import sys
import screed_tst_utils as utils
import screed
import screed.openscreed


def test_empty_open():
    filename = utils.get_test_data('empty.fa')
    assert len(list(iter(screed.open(filename)))) == 0


def test_simple_open():
    filename = utils.get_test_data('test.fa')

    n = -1
    for n, record in enumerate(screed.open(filename)):
        assert record.name == 'ENSMICT00000012722'
        break
    assert n == 0, n


def test_simple_open_fq():
    filename = utils.get_test_data('test.fastq')

    n = -1
    for n, record in enumerate(screed.open(filename)):
        assert record.name == 'HWI-EAS_4_PE-FC20GCB:2:1:492:573/2'
        break
    assert n == 0


def test_gz_open():
    filename1 = utils.get_test_data('test.fa')
    filename2 = utils.get_test_data('test.fa.gz')
    for n, (r1, r2) in enumerate(zip(screed.open(filename1),
                                     screed.open(filename2))):
        assert r1.name == r2.name

    assert n > 0


def test_bz2_open():
    filename1 = utils.get_test_data('test.fa')
    filename2 = utils.get_test_data('test.fa.bz2')
    for n, (r1, r2) in enumerate(zip(screed.open(filename1),
                                     screed.open(filename2))):
        assert r1.name == r2.name

    assert n > 0


def test_gz_open_fastq():
    filename1 = utils.get_test_data('test.fastq')
    filename2 = utils.get_test_data('test.fastq.gz')
    for n, (r1, r2) in enumerate(zip(screed.open(filename1),
                                     screed.open(filename2))):
        assert r1.name == r2.name

    assert n > 0


def test_get_writer_class_fasta():
    import screed.fasta

    filename = utils.get_test_data('test.fa')

    read_iter = screed.open(filename)
    x = screed.openscreed.get_writer_class(read_iter)
    assert x is screed.fasta.FASTA_Writer, x


def test_unknown_fileformat():

    try:
        screed.open(__file__)
    except ValueError as err:
        assert "unknown file format" in str(err)
