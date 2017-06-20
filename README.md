# Rest_API
REST API for people counting at the bus stop

**Show cams**
----
  Returns XML data about all cameras.

* **URL**

  /cams

* **Method:**

  `GET`
  
*  **URL Params**
      None
   <!--**Required:**-->
 
   <!--`id=[integer]`-->

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    <pre><code>`<cams>
        <cam id="1" name="cam1">
            <value timestamp="1496869786.02">17</value>
        </cam>
        <cam id="2" name="cam2">
            <value timestamp="1496869786.02">17</value>
        </cam>
    </cams>`
    </code></pre>
* **Error Response:**

  * **Code:** 401 <br />
    **Content:** `{ error : "Resource not available" }`

  <!--OR-->

  <!--* **Code:** 401 UNAUTHORIZED <br />-->
    <!--**Content:** `{ error : "You are unauthorized to make this request." }`-->

* **Sample Call:**

    ```javascript
    $.ajax({
      url: "/cams",
      dataType: "xml",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
    ```

**Show cam**
----
  Returns XML data about single camera.

* **URL**

  /cams/:id

* **Method:**

  `GET`
  
*  **URL Params**
   
   **Required:**
 
   `id=[integer]`

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    <pre><code> `<cam id="1" name="cam1">
        <value timestamp="1496869786.02">17</value>
        <value timestamp="1496869996.02">35</value>
     </cam>`</code></pre>
* **Error Response:**

  * **Code:** 410 <br />
    **Content:** `{ error : "Resource not available" }`

  <!--OR-->

  <!--* **Code:** 401 UNAUTHORIZED <br />-->
    <!--**Content:** `{ error : "You are unauthorized to make this request." }`-->

* **Sample Call:**

    ```javascript
    $.ajax({
      url: "/cams/1",
      dataType: "xml",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
    ```

**Avarage values from all cameras**
----
  Returns XML data to people on average from all cameras.

* **URL**

  /cams/avg

* **Method:**

  `GET`
  
*  **URL Params**
   None
   <!--**Required:**-->
 
   <!--`id=[integer]`-->

* **Data Params**

  **Required:**
   
     `start=[float]`
     `end=[float]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    <pre><code> `<cams>
      <cam id="1" name="cam1">
       <avg_value end_timestamp="1496869786.02" start_timestamp="1496868549.16">55</avg_value>
      </cam>
      <cam id="2" name="cam2">
       <avg_value end_timestamp="1496869786.02" start_timestamp="1496868549.16">41</avg_value>
      </cam>
     </cams>`</code></pre>
* **Error Response:**

  * **Code:** 410 <br />
    **Content:** `{ error : "No value" }`

  <!--OR-->

  <!--* **Code:** 401 UNAUTHORIZED <br />-->
    <!--**Content:** `{ error : "You are unauthorized to make this request." }`-->

* **Sample Call:**
    ```javascript
      $.ajax({
        url: "/cams/avg",
        data: { 
            "start": 1496869786.02, 
            "end": 1496868549.16, 
        },
        dataType: "xml",
        type : "GET",
        success : function(r) {
          console.log(r);
        }
      });
    ```
  
  **Avarage values from specific camera**
  ----
    Returns XML data to people on average from one cameras.
  
  * **URL**
  
    /cams/:id/avg
  
  * **Method:**
  
    `GET`
    
  *  **URL Params**
     
     **Required:**
   
     `id=[integer]`
  
  * **Data Params**
  
    **Required:**
     
       `start=[float]`
       `end=[float]`
  
  * **Success Response:**
  
    * **Code:** 200 <br />
      **Content:**
      <pre><code> `<cams>
        <cam id="1" name="cam1">
         <avg_value end_timestamp="1496869786.02" start_timestamp="1496868549.16">55</avg_value>
        </cam>
       </cams>`</code></pre>
  * **Error Response:**
  
    * **Code:** 410 <br />
      **Content:** `{ error : "Resource not available" }`
  
    OR
  
    * **Code:** 410 <br />
      **Content:** `{ error : "No value" }`
  
  * **Sample Call:**
  
    ```javascript
      $.ajax({
        url: "/cams/1/avg",
        data: { 
            "start": 1496869786.02, 
            "end": 1496868549.16, 
        },
        dataType: "xml",
        type : "GET",
        success : function(r) {
          console.log(r);
        }
      });
    ```
