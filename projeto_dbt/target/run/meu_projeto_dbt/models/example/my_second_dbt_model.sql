

  create or replace view `analise-taxis-projeto`.`taxis_dataset`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `analise-taxis-projeto`.`taxis_dataset`.`my_first_dbt_model`
where id = 1;

