import speech_recognition as s
import random
import pyttsx3

#list of countries
countries = ['Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'America',
'Amsterdam',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape',
'Chad',
'Chile',
'China',
'Colombia',
'Comoros',
'Congo',
'CostaRica',
'Croatia',
'Cuba',
'Cyprus',
'Czech',
'Denmark',
'Djibouti',
'Dominica',
'Dominican',
'Timor',
'Ecuador',
'Egypt',
'Salvador',
'Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Coast',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'North Korea',
'South Korea ',
'Kosovo',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russian Federation',
'Rwanda',
'St Kitts & Nevis',
'St Lucia',
'Saint Vincent & the Grenadines',
'Samoa',
'San Marino',
'Sao Tome & Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Sudan',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Russia',
'Afghanistan',
'Amsterdam',
'Zimbabwe']
used_countries = []
engine = pyttsx3.init()
switch = 1
pointer = 1
while 1:
    #random letter 
     query = ""
     if switch == 1:
        randomc = random.choice(countries)
        s_w1 = "I CHOOSE THE COUNTRY", randomc
        print(s_w1)
        print("")
        engine.say(s_w1)
        engine.runAndWait()
        nlastletter = (len(randomc))
        lastletter = randomc[nlastletter-1]
        lastletter = lastletter.title()
        s_w2 = "Now name the country with starting letter" , lastletter
        print(s_w2)
        print("")
        engine.say(s_w2)
        engine.runAndWait()
        switch = 0
        countries.remove(randomc)
        used_countries.append(randomc)
     else:
        nuserlastletter = used_countries[-1]
        userlastletter = nuserlastletter[-1]
        userlastletter = userlastletter.title()
        new_list = [i for i in countries if i.upper().startswith(userlastletter)]
        randomc = random.choice(new_list)
        s_w3 = "I CHOOSE THE COUNTRY", randomc
        print(s_w3)
        print("")
        engine.say(s_w3)
        engine.runAndWait()
        nlastletter = (len(randomc))
        lastletter = randomc[nlastletter-1]
        lastletter = lastletter.title()
        s_w4 = "Now name the country with starting letter" , lastletter
        print(s_w4)
        print("")
        engine.say(s_w4)
        engine.runAndWait()
        switch = 0
        countries.remove(randomc)
        used_countries.append(randomc)
     while 1:
        try:
            #listening module 
            sr=s.Recognizer()
            print("Listening")
            print("")
            with s.Microphone() as m:
                audio = sr.listen(m)
                query = sr.recognize_google(audio,language='eng-in')
                #print(query)
                if query == "stop":
                    print("game ended")
                    engine.say("game ended")
                    engine.runAndWait()
                    quit()
                elif  query =="skip":
                    print("ROUND SKIPPED")
                    print("")
                    engine.say("Round skipped")
                    engine.runAndWait()
                    randomc = random.choice(countries)
                    userRandom = randomc
                    countries.remove(userRandom)
                    used_countries.append(userRandom)
                    switch = 0
                    print("Selecting Random Country Name")
                    print("")
                    engine.say("Selecting random country name")
                    engine.runAndWait()
                    break
        except Exception as e:
            print(e)
            query = input("enter the country name: ")
        userfirstletter = query[0]
        if userfirstletter == lastletter:
            try:
                found = countries.index(query)
                s_w6 = "ok",countries[found]
                print(s_w6, "Current Points: ", pointer)
                print("")
                engine.say(s_w6)
                engine.runAndWait()
                countries.remove(query)
                used_countries.append(query)
                pointer = pointer+1
                switch = 0
                break
            except Exception as e:
                try:
                    checker = used_countries.index(query)
                    cName = used_countries[checker]
                    if query == cName:
                        print("This country name is already used ")
                        print("")
                        engine.say("This country name is already used")
                        engine.runAndWait()
                    else:
                        print("No name in used_countries list")
                        print("")
                        engine.say("No name in used_countries list")
                        engine.runAndWait()
                except Exception as e:
                    print(e)
                    engine.say(e)
                    engine.runAndWait()
        
        else:
            s_w5 ="NAME THE COUNTRY WITH STARTING LETTER ",lastletter 
            print(s_w5)
            print("")
            engine.say(s_w5)
            engine.runAndWait()
switch = 0 
