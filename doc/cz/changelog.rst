Changelog
---------

- 0.3.0
	- automatické pořizovnání screenshotů při chybě nebo selhání
	- možnost opakovat test při chybě nebo selhání
	- log metoda (:ref:`log`)
	- metoda pro pořízení screenshotu (:ref:`screenshots`)
	- vyladění IE pro větší stabilitu
	- nové parametry spuštěcího příkazu (:ref:`runningtests`)

- 0.2.0
	- možnost parametrizovat spouštěcí příkaz **runwebtests** (:ref:`runningtests`)
	- vylepšené hledání v logu proxy (:ref:`workingwithproxy`)
	- možnost předat metodě **wait** argument untilFunc pro periodickou kontrolu nutnosti čekání (:ref:`waits`)
	- možnost generování XML reportu s výsledky testů (pro Jenkins)
	- opravena chyba klikání na element mimo viewport v IE8
	- vyřešen (snad) problém se zatuhnutou instancí browseru po doběhnutí testu (přidání timeoutu do nodeconfig.json)
- 0.1.0
	- první verze
