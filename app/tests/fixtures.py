events_xml_response = b"""<?xml version="1.0" encoding="UTF-8"?>
<eventList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" xsi:noNamespaceSchemaLocation="eventList.xsd">
   <output>
      <base_event base_event_id="291" sell_mode="online" title="Camela en concierto">
         <event event_start_date="2021-06-30T21:00:00" event_end_date="2021-06-30T21:30:00" event_id="291" sell_from="2020-07-01T00:00:00" sell_to="2021-06-30T20:00:00" sold_out="false">
            <zone zone_id="40" capacity="200" price="20.00" name="Platea" numbered="true" />
            <zone zone_id="38" capacity="0" price="15.00" name="Grada 2" numbered="false" />
            <zone zone_id="30" capacity="80" price="30.00" name="A28" numbered="true" />
         </event>
      </base_event>
      <base_event base_event_id="1591" sell_mode="online" organizer_company_id="1" title="Los Morancos">
         <event event_start_date="2021-07-31T20:00:00" event_end_date="2021-07-31T21:00:00" event_id="1642" sell_from="2021-06-26T00:00:00" sell_to="2021-07-31T19:50:00" sold_out="false">
            <zone zone_id="186" capacity="0" price="75.00" name="Amfiteatre" numbered="true" />
            <zone zone_id="186" capacity="12" price="65.00" name="Amfiteatre" numbered="false" />
         </event>
      </base_event>
      <base_event base_event_id="444" sell_mode="offline" organizer_company_id="1" title="Tributo a Juanito Valderrama">
         <event event_start_date="2021-09-30T20:00:00" event_end_date="2021-09-30T20:00:00" event_id="1642" sell_from="2021-02-10T00:00:00" sell_to="2021-09-31T19:50:00" sold_out="false">
            <zone zone_id="7" capacity="22" price="65.00" name="Amfiteatre" numbered="false" />
         </event>
      </base_event>
   </output>
</eventList>
"""  # noqa: E501

events_xml_invalid_date_response = b"""<?xml version="1.0" encoding="UTF-8"?>
<eventList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" xsi:noNamespaceSchemaLocation="eventList.xsd">
   <output>
      <base_event base_event_id="444" sell_mode="offline" organizer_company_id="1" title="Tributo a Juanito Valderrama">
         <event event_start_date="2021-09-31T20:00:00" event_end_date="2021-09-31T20:00:00" event_id="1642" sell_from="2021-02-10T00:00:00" sell_to="2021-09-31T19:50:00" sold_out="false">
            <zone zone_id="7" capacity="22" price="65.00" name="Amfiteatre" numbered="false" />
         </event>
      </base_event>
   </output>
</eventList>
"""  # noqa: E501
