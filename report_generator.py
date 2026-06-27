def generate_report(results):

    with open("report.txt", "w") as f:

        for item in results:

            f.write(item + "\n")

    print("Report Generated")