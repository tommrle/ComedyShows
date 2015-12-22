'use strict';

var React = require('react-native');
var {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight
} = React;

var CalendarPicker = require('react-native-calendar-picker');
var TestShow = require('../test_data/showObjectSample.json'); //Test

var showView = React.createClass({
  getInitialState: function() {
    return {
      date: new Date(),
    };
  },
  render: function(){
    var show = this.props.show;
    var show = TestShow; //Test
    var imageUrl = 'http://localhost:8080/' + show.imageUrl;
    return (
      <View style={ styles.container }>
        <Image source={{ uri: imageUrl }} style={ styles.cellImage } />
        <Text style={ styles.title }>{ show.title }</Text>
        <Text>Theater: { show.theater }</Text>
        <Text>Description: { show.descrip }</Text>
        <View style={ styles.buttonRow }>
          <TouchableHighlight style={ styles.button }>
            <Text style={ styles.buttonText }>Get Tickets</Text>
          </TouchableHighlight>
        </View>
        <CalendarPicker
          selectedDate = { this.state.date }
          enabledDates = { show.showTimesFormatted }/>
      </View>
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 64
  },
  cellImage: {
    height: 300
  },
  title: {
    fontWeight: 'bold'
  },
  buttonRow: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center'
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 20,
  },
  button: {
    justifyContent: 'center',
    margin: 10,
    borderWidth: 1,
    borderRadius: 3,
    borderColor: '#00aced',
    backgroundColor: '#00aced',
  }
});

module.exports = showView;