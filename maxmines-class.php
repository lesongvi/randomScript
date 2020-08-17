class MaxMinesAPI {
	const API_URL = 'https://api.maxmines.com';
	private $secret = null;
	public function __construct($secret) {
		if (strlen($secret) !== 40) {
			throw new Exception('Invalid Secret key');
		}
		$this->secret = $secret;
	}
  
	function get($path, $data = []) {
		$data['secret'] = $this->secret;
		$url = self::API_URL.$path.'?'.http_build_query($data);
		$response = $this->api_request($url, false, null);
		return json_decode($response);
	}
	
	function post($path, $data = []) {
		$data['secret'] = $this->secret;
		$context = http_build_query($data);
		$url = SELF::API_URL.$path;
		$response = $this->api_request($url, true, $context);
		return json_decode($response);
	}
	
	function api_request($url, bool $post, $context) {
	    $curl = curl_init();
	    curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_FAILONERROR, 1);
        curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36");
        curl_setopt($curl, CURLOPT_RETURNTRANSFER,1);
        curl_setopt($curl, CURLOPT_POST, $post);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $context);
        $result = curl_exec($curl);
        curl_close($curl);
        return $result;
	}
}
