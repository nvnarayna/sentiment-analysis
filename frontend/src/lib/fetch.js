export default async function fetch_sentiment(txt) {
    const url = './api/nlp'; 
  
    const data = {
        text:txt
    };
  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data), 
    };
  
    try {
      const response = await fetch(url, options);
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const responseData = await response.json();
  
      return responseData

    } catch (error) {
      console.error('Fetch Error:', error);
    }
    // return {
    //     pos:21.4,
    //     neg:31.6,
    //     neu:48,
    //     compound:"Neutral"
    // }
  }
  