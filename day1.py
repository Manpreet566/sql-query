SELECT MAX(daily_visits.user_count) AS max_user_visits_in_a_day
FROM (
    SELECT 
        DATE(llva.server_time) AS visit_date,
        COUNT(DISTINCT mlv.user_id) AS user_count
    FROM analyticsdatabase.pb_matomo_log_visit mlv
    LEFT JOIN analyticsdatabase.pb_matomo_log_link_visit_action llva 
        ON mlv.idvisit = llva.idvisit
    LEFT JOIN analyticsdatabase.pb_matomo_log_action mla1 
        ON llva.idaction_name = mla1.idaction
    LEFT JOIN analyticsdatabase.pb_matomo_log_action mla2 
        ON llva.idaction_event_action = mla2.idaction
    LEFT JOIN analyticsdatabase.pb_matomo_log_action mla3
        ON llva.idaction_event_category = mla3.idaction
    WHERE mla2.name = 'View'
      AND mla3.name = 'ContentDetailPage'
    GROUP BY DATE(llva.server_time)
)AS daily_visits;
