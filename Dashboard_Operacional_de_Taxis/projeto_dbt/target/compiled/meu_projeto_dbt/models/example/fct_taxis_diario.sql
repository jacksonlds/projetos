

select
    date(data_hora_partida) as data_partida,
    count(1) as total_viagens,
    -- Ajuste os nomes das colunas abaixo de acordo com o seu esquema real de dados se necessário:
    avg(distancia_viagem) as distancia_media,
    avg(valor_total) as valor_medio
from `analise-taxis-projeto`.`taxis_dataset`.`stg_taxis_trips`
group by 1
order by data_partida desc