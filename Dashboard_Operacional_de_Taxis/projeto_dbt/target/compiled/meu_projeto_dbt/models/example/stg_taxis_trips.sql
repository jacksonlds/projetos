

SELECT
    vendor_id AS id_fornecedor,
    pickup_datetime AS data_hora_partida,
    dropoff_datetime AS data_hora_chegada,
    passenger_count AS quantidade_passageiros,
    trip_distance AS distancia_viagem,
    total_amount AS valor_total
FROM
    `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2018`
WHERE
    trip_distance > 0
    AND total_amount > 0
    AND passenger_count IS NOT NULL