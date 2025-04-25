# 1
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll No", "Name", "Sub1", "Sub2", "Sub3"])
    writer.writerow([1, "Alice", 80, 85, 90])
    writer.writerow([2, "Bob", 75, 70, 80])
print("CSV file created.")

# 2
data_dict = {}
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = int(row["Sub1"]) + int(row["Sub2"]) + int(row["Sub3"])
        data_dict[row["Roll No"]] = {
            "Name": row["Name"],
            "Marks": [int(row["Sub1"]), int(row["Sub2"]), int(row["Sub3"])],
            "Total": total
        }
print("Student Data:", data_dict)

# 3
name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")
with open("contact.vcf", "w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write(f"N:{name};;;\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    f.write("END:VCARD\n")
print("VCF file created.")

# 4
os.makedirs("new_subdir", exist_ok=True)
shutil.copy("students.csv", "new_subdir/students.csv")
print("File copied to new subdirectory.")

# 5
with open("students.csv", "r") as source, open("copy.csv", "w") as target:
    for line in source:
        target.write(line.upper())
print("Contents copied in uppercase.")

# 6
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("A1\nA2\nA3\n")
    f2.write("B1\nB2\n")

with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    maxlen = max(len(lines1), len(lines2))
    for i in range(maxlen):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])
print("Files merged.")

# 7
class Employee:
    def _init_(self, code, name, doj, salary):
        self.empcode = code
        self.empname = name
        self.doj = doj
        self.salary = salary

emp = Employee("E01", "John Doe", "2020-05-20", 55000)
with open("employee.dat", "wb") as f:
    pickle.dump(emp, f)

with open("employee.dat", "rb") as f:
    loaded = pickle.load(f)
    print("Deserialized Employee:", loaded._dict_)

# 8
with open("text.txt", "w") as f:
    f.write("This is a sample text with the word the, an and a.")

with open("text.txt", "r") as f:
    content = f.read()

words_to_remove = {"a", "the", "an"}
updated = ' '.join(["" if word.lower() in words_to_remove else word for word in content.split()])

with open("updated_text.txt", "w") as f:
    f.write(updated)
print("Filtered text written to new file.")
