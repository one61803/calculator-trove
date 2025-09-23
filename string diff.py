"123456789A123456789B123456789C123456789D123456789E123456789F123456789G123456789H123456789I123456789J123456789"
grid = {}
thread = {}
trace_1 = False
t_2 = False

"""Example:
diff("What did you do today?", "What did you all do today?")
 What did you do today?
 ======================
 What did you all do today?
 ============++++==========

 diff("ABGDEZHΘIKLMNΞOPQRSTUVX$W", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
 ABGDEZHΘIKLMNΞOPQRSTUVX$W
 ==-==-=-=====-=========--
 ABCDEFGHIJKLMNOPQRSTUVWXYZ
 ==+==++==+============+=++

diff("ABGDEFZH8IKLMN3OPQRSTUVX$W", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
 ABGDEFZH8IKLMN3OPQRSTUVX$W
 ==-===-=-=====-=========--
 ABCDEFGHIJKLMNOPQRSTUVWXYZ
 ==+===+==+============+=++

 diff("September", "settembre")
 September
 -=-=====-
 settembre
 +=+====+=

 diff("What did you do today?", "What did you do all day?")
 What did you do today?
 ================--====
 What did you do all day?
 ===============++++=====

 diff("FU8ARK", "ABGDEFZH8IK")
 FU8ARK
 =-=--=
 ABGDEFZH8IK
 +++++=++=+=

 diff("GWHNIY4PZS", "ZH8IKLMN3OPRS")
 GWHNIY4PZS
 --==---=-=
 ZH8IKLMN3OPRS
 +=+++++=++=+=

 diff("TVEML^DO", "TUVX$O")
 TVEML^DO
 ==-----=
 TUVX$O
 =+=++=

 diff("fictive", "fricative")
 fictive
 =======
 fricative
 =+==+====

 diff("octave", "astrolabe")
 octave
 =--=-=
 astrolabe
 ++++=+=+=

 diff("perspicacity", "perspicuity")
 perspicacity
 =======--===
 perspicuity
 =======+===

 diff("literati", "glitterati")
 literati
 ========
 glitterati
 +==+======

 diff("glittering", "glitterati")
 glittering
 ========--
 glitterati
 =======++=
 """


def input_y_or_n(message_ST):
    "Asks for a 'y' or 'n' input and loops until it gets a proper answer."
    ans_CH = ""
    while not (ans_CH in ["y", "n"]):
        ans_CH = input(message_ST)
        if not (ans_CH in ["y", "n"]):
            print("Error. Please answer with either 'y' or 'n'.\n")
    return ans_CH

def LCS(Gr, La, m, n):
    global grid, thread
    lett_1 = Gr[m]
    lett_2 = La[n]
    if (m == 0) or (n == 0):
        thread[2 ** m * 3 ** n] = "0"
        return 0
    location = 2**m * 3**n
    if location in grid:
        return grid[location]
    else:
        answ = (lett_1 == lett_2)
        if answ:
            value =  1 + LCS(Gr, La, m - 1, n - 1)
            out_ST = f"{m},{n},{value}"
            TRACE(trace_1, out_ST)
            grid[location] = value
            thread[location] = thread[2 ** (m - 1) * 3 ** (n - 1)] + ";" + out_ST            
            return value
        else:
            first = LCS(Gr, La, m - 1, n)
            second = LCS(Gr, La, m, n - 1)
            value = max(first, second)
            out_ST = f"{m},{n},{value}"
            TRACE(trace_1, out_ST)
            grid[location] = value
            if (first >= second):
                thread[location] = thread[2 ** (m - 1) * 3 ** n] + ";" + out_ST
            else:
                thread[location] = thread[2 ** m * 3 ** (n - 1)] + ";" + out_ST          
            return value

def process_thread(Gr, La, string_ST):
    triplets_LSST = string_ST.split(";")
    triplets_LSTR = []
    for element_ST in triplets_LSST:
        triplets_LSTR.append(element_ST.split(","))
    string_1 = ""
    string_2 = ""
    counts = [0,0,0]
    first_time_BL = True
    for triplet_TR in triplets_LSTR:
        TRACE(t_2, f"triplet_TR = {triplet_TR}")
        TRACE(t_2, f"counts = {counts}")
        if first_time_BL:
            first_time_BL = False
            TRACE(t_2, f"L114. first_time_BL = {first_time_BL}")
            if (int(triplet_TR[2]) == 1):
                TRACE(t_2, f"L116. triplet_TR[2] = {triplet_TR[2]}")
                if (int(triplet_TR[1]) > 1):
                    string_2 += "+"*(int(triplet_TR[1]) - 1)
                    TRACE(t_2, f"L120. string_2 = {string_2}")
                if (int(triplet_TR[0]) > 1):
                    string_1 += "-"*(int(triplet_TR[0]) - 1)
                    TRACE(t_2, f"L124. string_1 = {string_1}")
        if (int(triplet_TR[2]) > counts[2]):
            counts[2] = int(triplet_TR[2])
            counts[1] = int(triplet_TR[1])
            counts[0] = int(triplet_TR[0])
            string_1 += "="
            string_2 += "="
            TRACE(t_2, Gr)
            TRACE(t_2, " " + string_1)
            TRACE(t_2, La)
            TRACE_input(t_2, " " + string_2)
        else:
            if (int(triplet_TR[1]) > counts[1]):
                string_2 += "+"
                counts[1] = int(triplet_TR[1])
                TRACE(t_2, Gr)
                TRACE(t_2, " " + string_1)                  
                TRACE(t_2, La)
                TRACE_input(t_2, " " + string_2)              
            if (int(triplet_TR[0]) > counts[0]):
                string_1 += "-"
                counts[0] = int(triplet_TR[0])
                TRACE(t_2, Gr)
                TRACE(t_2, " " + string_1)
                TRACE(t_2, La)
                TRACE_input(t_2, " " + string_2)                
    print(Gr)
    print(" " + string_1)
    print(La)
    print(" " + string_2)

def diff(string_1_ST, string_2_ST):
    global grid, thread
    grid = {}
    thread = {}
    len_1_NT = len(string_1_ST)
    len_2_NT = len(string_2_ST)
    Gr_ST = " " + string_1_ST
    La_ST = " " + string_2_ST
    LCS(Gr_ST, La_ST, len_1_NT, len_2_NT)
    where_NT = 2 ** len_1_NT * 3 ** len_2_NT
    thread_ST = thread[where_NT]
    "Remove '0;' from the beginning of thread_ST."
    thread_ST = thread_ST[2:]
    TRACE(t_2, thread_ST)
    process_thread(Gr_ST, La_ST, thread_ST)

def TRACE(switch_BL, message_ST):
    if switch_BL:
        print(message_ST)

def TRACE_input(switch_BL, message_ST):
    if switch_BL:
        input(message_ST)
        
"FINIS · PROGRAMMATIS · FINIS · PROGRAMMATIS · FINIS · PROGRAMMATIS · FINIS · PROGRAMMATIS · PRO"
