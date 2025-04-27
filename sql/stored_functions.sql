create OR replace function get_rainy_days(current_month int, current_year int)
returns integer as $$
begin
  return (
    select count(*)
    from (
      select date(created_at)
      from weather_data
      where extract(month from created_at) = current_month
        and extract(year from created_at) = current_year
        and condition_text = 'Rain'
      group by date(created_at)
    ) as rainy_days
  );
end;
$$ language plpgsql

create or replace function hour_avg_temp(current_hour int, current_month int, current_year int)
returns float as $$
begin
  return (
    select avg(temperature_c)
    from weather_data
    where extract(hour from created_at) = current_hour
    and extract(month from created_at) = current_month 
    and extract(year from created_at) = current_year
  );
  end;
  $$ language plpgsql


create or replace function day_max(current_day int, current_month int, current_year int)
returns float as $$
begin
  return (
    select max(temperature_c)
    from weather_data
    where extract(day from created_at) = current_day 
    and extract(month from created_at) = current_month 
    and extract(year from created_at) = current_year
  );
  end;
  $$ language plpgsql


create or replace function day_min(current_day int, current_month int, current_year int)
returns float as $$
begin
  return (
    select min(temperature_c)
    from weather_data
    where extract(day from created_at) = current_day 
    and extract(month from created_at) = current_month 
    and extract(year from created_at) = current_year
  );
  end;
  $$ language plpgsql

create or replace function count_cold_days (current_month int, current_year int)
returns integer as $$
begin
  return (
    select count (*)
    from (
      select date(created_at)
      from weather_data
      where extract(month from created_at) = current_month 
      and extract(year from created_at) = current_year 
      and temperature_c <= 0
      group by date(created_at)
    ) as cold_days
  );
end;
$$ language plpgsql

create or replace function count_warm_days (current_month int, current_year int)
returns integer as $$
begin
  return (
    select count (*)
    from (
      select date(created_at)
      from weather_data
      where extract(month from created_at) = current_month and extract(year from created_at) = current_year and
      temperature_c >= 35
      group by date(created_at)
    ) as warm_days
  );
end;
$$ language plpgsql
