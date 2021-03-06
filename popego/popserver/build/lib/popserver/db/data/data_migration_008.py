__docformat__ = "restructuredtext"

migration = [
    ("""\
INSERT INTO countries (id, name) VALUES ('--', 'None, I''m a citizen of the world.');
INSERT INTO countries (id, name) VALUES ('ad', 'Andorra');
INSERT INTO countries (id, name) VALUES ('ae', 'United Arab Emirates');
INSERT INTO countries (id, name) VALUES ('af', 'Afghanistan');
INSERT INTO countries (id, name) VALUES ('ag', 'Antigua and Barbuda');
INSERT INTO countries (id, name) VALUES ('ai', 'Anguilla');
INSERT INTO countries (id, name) VALUES ('al', 'Albania');
INSERT INTO countries (id, name) VALUES ('am', 'Armenia');
INSERT INTO countries (id, name) VALUES ('an', 'Netherlands Antilles');
INSERT INTO countries (id, name) VALUES ('ao', 'Angola');
INSERT INTO countries (id, name) VALUES ('aq', 'Antarctica');
INSERT INTO countries (id, name) VALUES ('ar', 'Argentina');
INSERT INTO countries (id, name) VALUES ('as', 'American Samoa');
INSERT INTO countries (id, name) VALUES ('at', 'Austria');
INSERT INTO countries (id, name) VALUES ('au', 'Australia');
INSERT INTO countries (id, name) VALUES ('aw', 'Aruba');
INSERT INTO countries (id, name) VALUES ('az', 'Azerbaijan');
INSERT INTO countries (id, name) VALUES ('ba', 'Bosnia and Herzegowina');
INSERT INTO countries (id, name) VALUES ('bb', 'Barbados');
INSERT INTO countries (id, name) VALUES ('bd', 'Bangladesh');
INSERT INTO countries (id, name) VALUES ('be', 'Belgium');
INSERT INTO countries (id, name) VALUES ('bf', 'Burkina Faso');
INSERT INTO countries (id, name) VALUES ('bg', 'Bulgaria');
INSERT INTO countries (id, name) VALUES ('bh', 'Bahrain');
INSERT INTO countries (id, name) VALUES ('bi', 'Burundi');
INSERT INTO countries (id, name) VALUES ('bj', 'Benin');
INSERT INTO countries (id, name) VALUES ('bm', 'Bermuda');
INSERT INTO countries (id, name) VALUES ('bn', 'Brunei Darussalam');
INSERT INTO countries (id, name) VALUES ('bo', 'Bolivia');
INSERT INTO countries (id, name) VALUES ('br', 'Brazil');
INSERT INTO countries (id, name) VALUES ('bs', 'Bahamas');
INSERT INTO countries (id, name) VALUES ('bt', 'Bhutan');
INSERT INTO countries (id, name) VALUES ('bv', 'Bouvet Island');
INSERT INTO countries (id, name) VALUES ('bw', 'Botswana');
INSERT INTO countries (id, name) VALUES ('by', 'Belarus');
INSERT INTO countries (id, name) VALUES ('bz', 'Belize');
INSERT INTO countries (id, name) VALUES ('ca', 'Canada');
INSERT INTO countries (id, name) VALUES ('cc', 'Cocos (Keeling) Islands');
INSERT INTO countries (id, name) VALUES ('cd', 'Congo, the Democratic Republic of the');
INSERT INTO countries (id, name) VALUES ('cf', 'Central African Republic');
INSERT INTO countries (id, name) VALUES ('cg', 'Congo');
INSERT INTO countries (id, name) VALUES ('ch', 'Switzerland');
INSERT INTO countries (id, name) VALUES ('ci', 'Cote d''Ivoire');
INSERT INTO countries (id, name) VALUES ('ck', 'Cook Islands');
INSERT INTO countries (id, name) VALUES ('cl', 'Chile');
INSERT INTO countries (id, name) VALUES ('cm', 'Cameroon');
INSERT INTO countries (id, name) VALUES ('cn', 'China');
INSERT INTO countries (id, name) VALUES ('co', 'Colombia');
INSERT INTO countries (id, name) VALUES ('cr', 'Costa Rica');
INSERT INTO countries (id, name) VALUES ('cu', 'Cuba');
INSERT INTO countries (id, name) VALUES ('cv', 'Cape Verde');
INSERT INTO countries (id, name) VALUES ('cx', 'Christmas Island');
INSERT INTO countries (id, name) VALUES ('cy', 'Cyprus');
INSERT INTO countries (id, name) VALUES ('cz', 'Czech Republic');
INSERT INTO countries (id, name) VALUES ('de', 'Germany');
INSERT INTO countries (id, name) VALUES ('dj', 'Djibouti');
INSERT INTO countries (id, name) VALUES ('dk', 'Denmark');
INSERT INTO countries (id, name) VALUES ('dm', 'Dominica');
INSERT INTO countries (id, name) VALUES ('do', 'Dominican Republic');
INSERT INTO countries (id, name) VALUES ('dz', 'Algeria');
INSERT INTO countries (id, name) VALUES ('ec', 'Ecuador');
INSERT INTO countries (id, name) VALUES ('ee', 'Estonia');
INSERT INTO countries (id, name) VALUES ('eg', 'Egypt');
INSERT INTO countries (id, name) VALUES ('eh', 'Western Sahara');
INSERT INTO countries (id, name) VALUES ('er', 'Eritrea');
INSERT INTO countries (id, name) VALUES ('es', 'Spain');
INSERT INTO countries (id, name) VALUES ('et', 'Ethiopia');
INSERT INTO countries (id, name) VALUES ('fi', 'Finland');
INSERT INTO countries (id, name) VALUES ('fj', 'Fiji');
INSERT INTO countries (id, name) VALUES ('fk', 'Falkland Islands (Malvinas)');
INSERT INTO countries (id, name) VALUES ('fm', 'Micronesia, Federated States of');
INSERT INTO countries (id, name) VALUES ('fo', 'Faroe Islands');
INSERT INTO countries (id, name) VALUES ('fr', 'France');
INSERT INTO countries (id, name) VALUES ('fx', 'France, Metropolitan');
INSERT INTO countries (id, name) VALUES ('ga', 'Gabon');
INSERT INTO countries (id, name) VALUES ('gb', 'United Kingdom');
INSERT INTO countries (id, name) VALUES ('gd', 'Grenada');
INSERT INTO countries (id, name) VALUES ('ge', 'Georgia');
INSERT INTO countries (id, name) VALUES ('gf', 'French Guiana');
INSERT INTO countries (id, name) VALUES ('gh', 'Ghana');
INSERT INTO countries (id, name) VALUES ('gi', 'Gibraltar');
INSERT INTO countries (id, name) VALUES ('gl', 'Greenland');
INSERT INTO countries (id, name) VALUES ('gm', 'Gambia');
INSERT INTO countries (id, name) VALUES ('gn', 'Guinea');
INSERT INTO countries (id, name) VALUES ('gp', 'Guadeloupe');
INSERT INTO countries (id, name) VALUES ('gq', 'Equatorial Guinea');
INSERT INTO countries (id, name) VALUES ('gr', 'Greece');
INSERT INTO countries (id, name) VALUES ('gs', 'South Georgia and the South Sandwich Islands');
INSERT INTO countries (id, name) VALUES ('gt', 'Guatemala');
INSERT INTO countries (id, name) VALUES ('gu', 'Guam');
INSERT INTO countries (id, name) VALUES ('gw', 'Guinea-Bissau');
INSERT INTO countries (id, name) VALUES ('gy', 'Guyana');
INSERT INTO countries (id, name) VALUES ('hk', 'Hong Kong');
INSERT INTO countries (id, name) VALUES ('hm', 'Heard and Mc Donald Islands');
INSERT INTO countries (id, name) VALUES ('hn', 'Honduras');
INSERT INTO countries (id, name) VALUES ('hr', 'Croatia (Hrvatska)');
INSERT INTO countries (id, name) VALUES ('ht', 'Haiti');
INSERT INTO countries (id, name) VALUES ('hu', 'Hungary');
INSERT INTO countries (id, name) VALUES ('id', 'Indonesia');
INSERT INTO countries (id, name) VALUES ('ie', 'Ireland');
INSERT INTO countries (id, name) VALUES ('il', 'Israel');
INSERT INTO countries (id, name) VALUES ('in', 'India');
INSERT INTO countries (id, name) VALUES ('io', 'British Indian Ocean Territory');
INSERT INTO countries (id, name) VALUES ('iq', 'Iraq');
INSERT INTO countries (id, name) VALUES ('ir', 'Iran (Islamic Republic of)');
INSERT INTO countries (id, name) VALUES ('is', 'Iceland');
INSERT INTO countries (id, name) VALUES ('it', 'Italy');
INSERT INTO countries (id, name) VALUES ('jm', 'Jamaica');
INSERT INTO countries (id, name) VALUES ('jo', 'Jordan');
INSERT INTO countries (id, name) VALUES ('jp', 'Japan');
INSERT INTO countries (id, name) VALUES ('ke', 'Kenya');
INSERT INTO countries (id, name) VALUES ('kg', 'Kyrgyzstan');
INSERT INTO countries (id, name) VALUES ('kh', 'Cambodia');
INSERT INTO countries (id, name) VALUES ('ki', 'Kiribati');
INSERT INTO countries (id, name) VALUES ('km', 'Comoros');
INSERT INTO countries (id, name) VALUES ('kn', 'Saint Kitts and Nevis');
INSERT INTO countries (id, name) VALUES ('kp', 'Korea, Democratic People''s Republic of');
INSERT INTO countries (id, name) VALUES ('kr', 'Korea, Republic of');
INSERT INTO countries (id, name) VALUES ('kw', 'Kuwait');
INSERT INTO countries (id, name) VALUES ('ky', 'Cayman Islands');
INSERT INTO countries (id, name) VALUES ('kz', 'Kazakhstan');
INSERT INTO countries (id, name) VALUES ('la', 'Lao People''s Democratic Republic');
INSERT INTO countries (id, name) VALUES ('lb', 'Lebanon');
INSERT INTO countries (id, name) VALUES ('lc', 'Saint Lucia');
INSERT INTO countries (id, name) VALUES ('li', 'Liechtenstein');
INSERT INTO countries (id, name) VALUES ('lk', 'Sri Lanka');
INSERT INTO countries (id, name) VALUES ('lr', 'Liberia');
INSERT INTO countries (id, name) VALUES ('ls', 'Lesotho');
INSERT INTO countries (id, name) VALUES ('lt', 'Lithuania');
INSERT INTO countries (id, name) VALUES ('lu', 'Luxembourg');
INSERT INTO countries (id, name) VALUES ('lv', 'Latvia');
INSERT INTO countries (id, name) VALUES ('ly', 'Libyan Arab Jamahiriya');
INSERT INTO countries (id, name) VALUES ('ma', 'Morocco');
INSERT INTO countries (id, name) VALUES ('mc', 'Monaco');
INSERT INTO countries (id, name) VALUES ('md', 'Moldova, Republic of');
INSERT INTO countries (id, name) VALUES ('mg', 'Madagascar');
INSERT INTO countries (id, name) VALUES ('mh', 'Marshall Islands');
INSERT INTO countries (id, name) VALUES ('mk', 'Macedonia, The Former Yugoslav Republic of');
INSERT INTO countries (id, name) VALUES ('ml', 'Mali');
INSERT INTO countries (id, name) VALUES ('mm', 'Myanmar');
INSERT INTO countries (id, name) VALUES ('mn', 'Mongolia');
INSERT INTO countries (id, name) VALUES ('mo', 'Macau');
INSERT INTO countries (id, name) VALUES ('mp', 'Northern Mariana Islands');
INSERT INTO countries (id, name) VALUES ('mq', 'Martinique');
INSERT INTO countries (id, name) VALUES ('mr', 'Mauritania');
INSERT INTO countries (id, name) VALUES ('ms', 'Montserrat');
INSERT INTO countries (id, name) VALUES ('mt', 'Malta');
INSERT INTO countries (id, name) VALUES ('mu', 'Mauritius');
INSERT INTO countries (id, name) VALUES ('mv', 'Maldives');
INSERT INTO countries (id, name) VALUES ('mw', 'Malawi');
INSERT INTO countries (id, name) VALUES ('mx', 'Mexico');
INSERT INTO countries (id, name) VALUES ('my', 'Malaysia');
INSERT INTO countries (id, name) VALUES ('mz', 'Mozambique');
INSERT INTO countries (id, name) VALUES ('na', 'Namibia');
INSERT INTO countries (id, name) VALUES ('nc', 'New Caledonia');
INSERT INTO countries (id, name) VALUES ('ne', 'Niger');
INSERT INTO countries (id, name) VALUES ('nf', 'Norfolk Island');
INSERT INTO countries (id, name) VALUES ('ng', 'Nigeria');
INSERT INTO countries (id, name) VALUES ('ni', 'Nicaragua');
INSERT INTO countries (id, name) VALUES ('nl', 'Netherlands');
INSERT INTO countries (id, name) VALUES ('no', 'Norway');
INSERT INTO countries (id, name) VALUES ('np', 'Nepal');
INSERT INTO countries (id, name) VALUES ('nr', 'Nauru');
INSERT INTO countries (id, name) VALUES ('nu', 'Niue');
INSERT INTO countries (id, name) VALUES ('nz', 'New Zealand');
INSERT INTO countries (id, name) VALUES ('om', 'Oman');
INSERT INTO countries (id, name) VALUES ('pa', 'Panama');
INSERT INTO countries (id, name) VALUES ('pe', 'Peru');
INSERT INTO countries (id, name) VALUES ('pf', 'French Polynesia');
INSERT INTO countries (id, name) VALUES ('pg', 'Papua New Guinea');
INSERT INTO countries (id, name) VALUES ('ph', 'Philippines');
INSERT INTO countries (id, name) VALUES ('pk', 'Pakistan');
INSERT INTO countries (id, name) VALUES ('pl', 'Poland');
INSERT INTO countries (id, name) VALUES ('pm', 'St. Pierre and Miquelon');
INSERT INTO countries (id, name) VALUES ('pn', 'Pitcairn');
INSERT INTO countries (id, name) VALUES ('pr', 'Puerto Rico');
INSERT INTO countries (id, name) VALUES ('pt', 'Portugal');
INSERT INTO countries (id, name) VALUES ('pw', 'Palau');
INSERT INTO countries (id, name) VALUES ('py', 'Paraguay');
INSERT INTO countries (id, name) VALUES ('qa', 'Qatar');
INSERT INTO countries (id, name) VALUES ('re', 'Reunion');
INSERT INTO countries (id, name) VALUES ('ro', 'Romania');
INSERT INTO countries (id, name) VALUES ('ru', 'Russian Federation');
INSERT INTO countries (id, name) VALUES ('rw', 'Rwanda');
INSERT INTO countries (id, name) VALUES ('sa', 'Saudi Arabia');
INSERT INTO countries (id, name) VALUES ('sb', 'Solomon Islands');
INSERT INTO countries (id, name) VALUES ('sc', 'Seychelles');
INSERT INTO countries (id, name) VALUES ('sd', 'Sudan');
INSERT INTO countries (id, name) VALUES ('se', 'Sweden');
INSERT INTO countries (id, name) VALUES ('sg', 'Singapore');
INSERT INTO countries (id, name) VALUES ('sh', 'St. Helena');
INSERT INTO countries (id, name) VALUES ('si', 'Slovenia');
INSERT INTO countries (id, name) VALUES ('sj', 'Svalbard and Jan Mayen Islands');
INSERT INTO countries (id, name) VALUES ('sk', 'Slovakia (Slovak Republic)');
INSERT INTO countries (id, name) VALUES ('sl', 'Sierra Leone');
INSERT INTO countries (id, name) VALUES ('sm', 'San Marino');
INSERT INTO countries (id, name) VALUES ('sn', 'Senegal');
INSERT INTO countries (id, name) VALUES ('so', 'Somalia');
INSERT INTO countries (id, name) VALUES ('sr', 'Suriname');
INSERT INTO countries (id, name) VALUES ('st', 'Sao Tome and Principe');
INSERT INTO countries (id, name) VALUES ('sv', 'El Salvador');
INSERT INTO countries (id, name) VALUES ('sy', 'Syrian Arab Republic');
INSERT INTO countries (id, name) VALUES ('sz', 'Swaziland');
INSERT INTO countries (id, name) VALUES ('tc', 'Turks and Caicos Islands');
INSERT INTO countries (id, name) VALUES ('td', 'Chad');
INSERT INTO countries (id, name) VALUES ('tf', 'French Southern Territories');
INSERT INTO countries (id, name) VALUES ('tg', 'Togo');
INSERT INTO countries (id, name) VALUES ('th', 'Thailand');
INSERT INTO countries (id, name) VALUES ('tj', 'Tajikistan');
INSERT INTO countries (id, name) VALUES ('tk', 'Tokelau');
INSERT INTO countries (id, name) VALUES ('tm', 'Turkmenistan');
INSERT INTO countries (id, name) VALUES ('tn', 'Tunisia');
INSERT INTO countries (id, name) VALUES ('to', 'Tonga');
INSERT INTO countries (id, name) VALUES ('tp', 'East Timor');
INSERT INTO countries (id, name) VALUES ('tr', 'Turkey');
INSERT INTO countries (id, name) VALUES ('tt', 'Trinidad and Tobago');
INSERT INTO countries (id, name) VALUES ('tv', 'Tuvalu');
INSERT INTO countries (id, name) VALUES ('tw', 'Taiwan, Province of China');
INSERT INTO countries (id, name) VALUES ('tz', 'Tanzania, United Republic of');
INSERT INTO countries (id, name) VALUES ('ua', 'Ukraine');
INSERT INTO countries (id, name) VALUES ('ug', 'Uganda');
INSERT INTO countries (id, name) VALUES ('um', 'United States Minor Outlying Islands');
INSERT INTO countries (id, name) VALUES ('us', 'United States');
INSERT INTO countries (id, name) VALUES ('uy', 'Uruguay');
INSERT INTO countries (id, name) VALUES ('uz', 'Uzbekistan');
INSERT INTO countries (id, name) VALUES ('va', 'Holy See (Vatican City State)');
INSERT INTO countries (id, name) VALUES ('vc', 'Saint Vincent and the Grenadines');
INSERT INTO countries (id, name) VALUES ('ve', 'Venezuela');
INSERT INTO countries (id, name) VALUES ('vg', 'Virgin Islands (British)');
INSERT INTO countries (id, name) VALUES ('vi', 'Virgin Islands (U.S.)');
INSERT INTO countries (id, name) VALUES ('vn', 'Viet Nam');
INSERT INTO countries (id, name) VALUES ('vu', 'Vanuatu');
INSERT INTO countries (id, name) VALUES ('wf', 'Wallis and Futuna Islands');
INSERT INTO countries (id, name) VALUES ('ws', 'Samoa');
INSERT INTO countries (id, name) VALUES ('ye', 'Yemen');
INSERT INTO countries (id, name) VALUES ('yt', 'Mayotte');
INSERT INTO countries (id, name) VALUES ('yu', 'Yugoslavia');
INSERT INTO countries (id, name) VALUES ('za', 'South Africa');
INSERT INTO countries (id, name) VALUES ('zm', 'Zambia');
INSERT INTO countries (id, name) VALUES ('zw', 'Zimbabwe');
      """,
    """\
DELETE FROM countries;
    """),
]

