def check_admission(rank,college_name):
    print("----------------------")
    print("Analyzing parameters for " + college_name + "...")

    if rank <= 16000:
        print("Result: High probability under your Muslim quota reservation!")
    else:
        print("Result: Check backup safety strategies.")


check_admission(15545, "GECK Kozhikode")
check_admission(8200, "NSS Palakkad")
check_admission(24000,"Private Self-Financing")
check_admission(5000, "CET Trivandrum")