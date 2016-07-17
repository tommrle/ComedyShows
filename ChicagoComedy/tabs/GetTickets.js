'use strict';

var React = require('react-native');
var {
  StyleSheet,
  Text,
  View,
  TouchableHighlight
} = React;

var CalendarPicker = require('react-native-calendar-picker');
var TestShow = require('../test_data/showObjectSample.json');
var show = TestShow;

var getTickets = React.createClass({
  getInitialState: function() {
    return {
      date: new Date(show.nextShowTime),
    };
  },
  onDateChange: function(date) {
    this.setState({ date: date });
    var showTimeButtons = <Text style={ styles.button }>Buy Tickets</Text>;
    this.setState({ showTimeButtons: showTimeButtons });
  },
  createShowTimeButtons: function() {
    var date = this.state.date;
    var showTimes = show.showTimeCal[date.getFullYear()][date.getMonth()][date.getDate()];
    this.state.showTimes = showTimes;
  },
  render: function() {
    this.createShowTimeButtons();
    return (
      <View style={ styles.container }>
        <CalendarPicker
          selectedDate = { this.state.date }
          onDateChange = { this.onDateChange }
          enabledDates = { show.showTimeCal } />
        <Text> { this.state.date.toString() } </Text>
      </View>
    );
  }

});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 60
  },
  button: {
    textAlign: 'center',
    
    height: 60,
    width: 120,
    backgroundColor: '#77f',
    
    
    
  }
})

module.exports = getTickets;