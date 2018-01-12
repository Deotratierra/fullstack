#!/usr/bin/ruby

require "test/unit"
require_relative "youtube"

# Configuración de los tests
class TestConfig
    def initialize
        @YOUTUBE_API_KEY = ENV["YOUTUBE_API_KEY"]
        @MY_CHANNEL_ID = "UCAgyf7c-giXPM0zgEExB74w"
        @VIDEO_URL = "https://www.youtube.com/watch?v=zAPEHIzHPT4"
    end
    attr_reader :YOUTUBE_API_KEY, :MY_CHANNEL_ID, :VIDEO_URL
end

$config = TestConfig.new
$client = YoutubeApi.new($config.YOUTUBE_API_KEY)

class TestYoutubeApi < Test::Unit::TestCase
    def test_channel_videos
        assert_instance_of(Array, 
                           $client.channel_videos($config.MY_CHANNEL_ID))        
    end

    def test_search_channel
        assert_instance_of(Hash, 
                           $client.search_channel($config.MY_CHANNEL_ID))
    end

    def test_search_video
        assert_instance_of(Hash, 
                           $client.search_video($config.VIDEO_URL))
    end

    def test_channel_video_urls
        assert_instance_of(Array, 
                           $client.channel_video_urls($config.MY_CHANNEL_ID))
    end

    def test_search_by_tag
        assert_instance_of(Array, 
                           $client.search_by_tag("Medicina germánica"))
    end

    def test_video_comments
        assert_instance_of(Hash, 
                           $client.video_comments($config.VIDEO_URL))
    end

end


=begin
- Para lanzar los tests:
ruby test.rb

- Para lanzar tests individuales:
ruby -w test.rb --name test_channel_videos

Fuente:
https://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing
=end
