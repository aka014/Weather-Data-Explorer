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


create or replace function get_last_data()
returns table (
    d date,
    t time,
    temp real,
    hum smallint,
    wind real,
    press smallint,
    condition text
) as $$
begin
    return query (
        select
            date(created_at),
            created_at::time,
            temperature_c,
            humidity,
            wind_speed,
            pressure,
            condition_text
        from weather_data
        order by id desc
        limit 12
    );
end;
$$ language plpgsql


CREATE OR REPLACE FUNCTION get_last_seven_days()
RETURNS TABLE (ts DATE, min_temp FLOAT, max_temp FLOAT) AS $$
BEGIN
  RETURN QUERY
    SELECT 
      date(created_at) as ts,  
      min(temperature_c)::float as min_temp,
      max(temperature_c)::float as max_temp
    FROM weather_data
    WHERE created_at >= now() - interval '8 days'  
      AND created_at < now() - interval '1 day'   
    GROUP BY date(weather_data.created_at)  
    ORDER BY ts desc
    LIMIT 7;
END;
$$ LANGUAGE plpgsql
