import argparse

parser = argparse.ArgumentParser(description='合計値を算出する引数処理です。')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='整数を計算します')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='整数の合計値を戻します。 (デフォルトは、最大値です。)')

args = parser.parse_args()
print(args.accumulate(args.integers))