create or replace function get_district (city varchar) 	returns varchar as $$
begin
	if (city = 'San Juan' or city = 'Aguas Buenas' or city = 'Guaynabo') then 
		return 'San Juan';
	elseif (city = 'Bayamon' or city = 'Catano' or city = 'Toa Alta' or city = 'Toa Baja') then
		return 'Bayamon';
	elseif (city = 'Arecibo' or city = 'Barceloneta' or city = 'Camuy' or city = 'Ciales' or city = 'Dorado' or city = 'Florida' or 
		city = 'Hatillo' or city = 'Manati' or city = 'Morovis' or city = 'Quebradillas' or city = 'Vega Alta' or city = 'Vega Baja') then
		return 'Arecibo';
	elseif (city = 'Aguada' or city = 'Aguadilla' or city = 'Anasco' or city = 'Cabo Rojo' or city = 'Hormigueros' or city = 'Isabela' or 
		city = 'Las Marias' or city = 'Mayaguez' or city = 'Moca' or city = 'Rincon' or city = 'San German' or city = 'San Sebastian') then
		return 'Mayaguez';
	elseif (city = 'Adjuntas' or city = 'Guanica' or city = 'Guayanilla' or city = 'Jayuya' or city = ' Juana Diaz' or city = 'Lajas' or 
		city = 'Lares' or city = 'Maricao' or city = 'Penuelas' or city = 'Ponce' or city = 'Sabana Grande' or city = 'Utuado' or city = 'Yauco') then
		return 'Ponce';
	elseif (city = 'Aibonito' or city = 'Arroyo' or city = 'Barranquitas' or city = 'Cayey' or city = 'Cidra' or city = 'Coamo' or 
		city = 'Comerio' or city = 'Corozal' or city = 'Guayama' or city = 'Naranjito' or city = 'Orocovis' or 
		city = 'Salinas' or city = 'Santa Isabel' or city = 'Villalba') then
		return 'Guayama';
	elseif (city = 'Caguas' or city = 'Gurabo' or city = 'Humacao' or city = 'Juncos' or city = 'Las Piedras' or city = 'Maunabo' or 
		city = 'Naguabo' or city = 'Patillas' or city = 'San Lorenzo' or city = 'Yabucoa') then
		return 'Humacao';
	elseif (city = 'Canovanas' or city = 'Carolina' or city = 'Ceiba' or city = 'Culebra' or city = 'Fajardo' or 
		city = 'Loiza' or city = 'Luquillo' or city = 'Rio Grande' or city = 'Trujillo Alto' or city = 'Vieques') then
		return 'Carolina';
	end if;
 end
$$ language plpgsql;