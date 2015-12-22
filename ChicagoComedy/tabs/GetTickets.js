'use strict';

var React = require('react-native');
var {
  StyleSheet,
  Text,
  View
} = React;

var CalendarPicker = require('react-native-calendar-picker');
var TestShow = require('../test_data/showObjectSample.json');

var getTickets = React.createClass({
  getInitialState: function() {
    return {
      date: new Date(),
    };
  },
  render: function() {
    var show = TestShow;
    var showTimes = TestShow.show_times;
    
    return (
      <View style={ styles.container }>
        <CalendarPicker
          selectedDate = { this.state.date }
          enabledDates = { show.showTimesFormatted } />
        <Text> { this.state.date.toString() } </Text>
        
      </View>
    );
  }

});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 60
  }
})

module.exports = getTickets;