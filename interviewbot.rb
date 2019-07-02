#
# Ruby automated interviewbot example
#
# Can you write a program that passes the interviewbot test?
#
require "net/http"
require "json"

def main
  # get started
  # get the path to the first question
  start_result = post_json('/interviewbot/start', { :login => 'your-login-here'})
  question_path = start_result['nextQuestion']

  loop do
  # Answer each question
    # get the next question
    question = get_json(question_path)

    # your code to figure out the answer goes here
    answer = answer_question(question)

    # send it to interviewbot
    answer_result = send_answer(question_path, answer)

    break if answer_result['result'] != 'correct'
    question_path = answer_result['nextQuestion']
  end
end

def answer_question(question)
  # your code to figure out the answer goes here
  'TODO: Implement answer_question'
end

def send_answer(path, answer)
  post_json(path, { :answer => answer })
end

# get data from the api and parse it into a ruby hash
def get_json(path)
  puts "*** GET #{path}"

  response = Net::HTTP.get_response(build_uri(path))
  result = JSON.parse(response.body)
  puts "HTTP #{response.code}"

  puts JSON.pretty_generate(result)
  result
end

# post an answer to the noops api
def post_json(path, body)
  uri = build_uri(path)
  puts "*** POST #{path}"
  puts JSON.pretty_generate(body)

  post_request = Net::HTTP::Post.new(uri, 'Content-Type' => 'application/json')
  post_request.body = JSON.generate(body)

  response = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => true) do |http|
    http.request(post_request)
  end

  puts "HTTP #{response.code}"
  result = JSON.parse(response.body)
  puts JSON.pretty_generate(result)
  result
end

def build_uri(path)
  domain = "https://api.noopschallenge.com"
  URI.parse(domain + path)
end

main()
