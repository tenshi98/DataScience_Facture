let
Origen=Csv.Document(File.Contents("datos_facturas.csv"),[Delimiter=",",Encoding=65001]),
PH=Table.PromoteHeaders(Origen),
Tipos=Table.TransformColumnTypes(PH,{{"fecha_factura",type date},{"proveedor",type text},{"concepto",type text},{"importe",type number},{"moneda",type text}})
in Tipos