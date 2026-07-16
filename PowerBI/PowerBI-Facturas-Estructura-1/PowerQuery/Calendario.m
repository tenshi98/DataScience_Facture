let
Inicio=#date(2024,1,1),Fin=#date(2030,12,31),Lista=List.Dates(Inicio,Duration.Days(Fin-Inicio)+1,#duration(1,0,0,0)),Tabla=Table.FromList(Lista,Splitter.SplitByNothing(),{"Date"})
in Tabla