from bs4 import BeautifulSoup
import requests
url = "https://admit.washington.edu/EquivalencyGuide/Pierce"
req = requests.get(url)
data = req.text
soup = BeautifulSoup(data, "html.parser")
uwArray = [];
ccArray = [];

for link in soup.find_all("td", {"class", "uwequiv"}):
    uwArray.append(link.getText());
    # print(link.getText());

for link in soup.find_all("td", {"class", "cccourse"}):
    ccArray.append(link.getText());
    # print(link.getText());

i = 0;
fw = open("output.txt", "w");
while (i < len(uwArray)):
    fw.write(uwArray[i]);
    print(uwArray[i])
    fw.write(",");
    fw.write(ccArray[i]);
    print(ccArray[i])
    fw.write("\n");
    i = i + 1;
fw.close();
print("Success")
