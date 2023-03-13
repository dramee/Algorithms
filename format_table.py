def format_table(benchmarks, algos, results):
    names = ["Benchmark"] + algos
    lengths = [len(max(benchmarks + ["Benchmark"], key=len))]
    for i in range(len(algos)):
        lengths.append(len(max([algos[i]] + [str(res[i]) for res in results], key=len)))
    for i in range(len(benchmarks) + 1):
        print("|", end="")
        for j in range(len(lengths)):
            if i == 0:
                print(f" {names[j]}" + " " * (1 + lengths[j] - len(names[j])), end="|")
            else:
                if j == 0:
                    print(f" {benchmarks[i - 1]}" + " " * (1 + lengths[j] - len(benchmarks[i - 1])), end="|")
                else:
                    print(f" {results[i-1][j-1]}" + " " * (1 + lengths[j] - len(str(results[i-1][j-1]))), end="|")
        if i == 0:
            print("\n" + "|" + "-" * ((-1 + sum(lengths)) + 3 * len(lengths)) + "|")
        else:
            print()
    pass


# format_table(["1", "1", "1"], ["quick sort", "merge sort", "bubble sort"],
#              [["geom mean: 1.23312314115141 mean: 1233123151251231231421, std deviation 312515314623624316", 1.56, 2.0], [2.23, 2.01, 2.8131231231321], [3.3, 2.9, 3.9]])