let
    Origen = Csv.Document(File.Contents("C:\Ruta\datos_facturas.csv"),
        [Delimiter=";", Columns=5, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    EncabezadosPromovidos = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    TiposCambiados = Table.TransformColumnTypes(EncabezadosPromovidos,{
        {"fecha_factura", type date},
        {"proveedor", type text},
        {"concepto", type text},
        {"importe", type number},
        {"moneda", type text}
    }),
    // Columnas auxiliares para el dashboard
    AgregarAnio = Table.AddColumn(TiposCambiados, "Anio", each Date.Year([fecha_factura]), Int64.Type),
    AgregarMes = Table.AddColumn(AgregarAnio, "Mes", each Date.Month([fecha_factura]), Int64.Type),
    AgregarNombreMes = Table.AddColumn(AgregarMes, "NombreMes", each Date.MonthName([fecha_factura]), type text),
    AgregarTrimestre = Table.AddColumn(AgregarNombreMes, "Trimestre", each "T" & Number.ToText(Date.QuarterOfYear([fecha_factura])), type text)
in
    AgregarTrimestre
