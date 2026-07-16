let
    FechaInicio = #date(2024,1,1),
    FechaFin = #date(2024,12,31),
    ListaFechas = List.Dates(FechaInicio, Duration.Days(FechaFin - FechaInicio) + 1, #duration(1,0,0,0)),
    TablaFechas = Table.FromList(ListaFechas, Splitter.SplitByNothing(), {"Fecha"}),
    TipoFecha = Table.TransformColumnTypes(TablaFechas,{{"Fecha", type date}}),
    AgregarAnio = Table.AddColumn(TipoFecha, "Anio", each Date.Year([Fecha]), Int64.Type),
    AgregarMes = Table.AddColumn(AgregarAnio, "Mes", each Date.Month([Fecha]), Int64.Type),
    AgregarNombreMes = Table.AddColumn(AgregarMes, "NombreMes", each Date.MonthName([Fecha]), type text),
    AgregarTrimestre = Table.AddColumn(AgregarNombreMes, "Trimestre", each "T" & Number.ToText(Date.QuarterOfYear([Fecha])), type text)
in
    AgregarTrimestre
