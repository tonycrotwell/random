#!/apps/perl5.6.1/bin/perl

use CGI;
use CGI::Carp 'fatalsToBrowser';

$query = new CGI;

$header = '<p><b><center><font color="#FF8040"><h1>Dew-Whacker Hacker Tracker</h1></font></center></b>';

$footer = '<p><b><h1><center><font color="#FF8040">This is the page footer</font></center></h1></b>';

$background = '<body bgcolor="#008000" text="#FFFFFF" link="#FFFF00"
vlink="#00FFFF">';


if ( $query->param('State') eq 'Lets Go!!!!!' ) { handicap_me() }
elsif ( $query->param('State') eq 'Enter New Score' ) { enter_new() }
elsif ( $query->param('State') eq 'View Handicap' ) { view_handi() }
elsif ( $query->param('State') eq 'Search by Score' ) { search_score() }
elsif ( $query->param('State') eq 'Search by Course' ) { search_course() }
elsif ( $query->param('State') eq 'Search by Date' ) { search_date() }
elsif ( $query->param('State') eq 'Submit Score' ) { calc_score() }
elsif ( $query->param('State') eq 'Enter Another Score' ) { enter_new() }
elsif ( $query->param('State') eq 'Return To Main Menu' ) { handicap_me() }
elsif ( $query->param('State') eq 'Show Scores' ) { show_scores() }
elsif ( $query->param('State') eq 'Show Dates' ) { show_dates() }
elsif ( $query->param('State') eq 'Show Course' ) { show_course() }
elsif ( $query->param('State') eq 'Search For Another Score' ) { search_score() }
elsif ( $query->param('State') eq 'Search For Another Date' ) { search_date() }
elsif ( $query->param('State') eq 'Search For Another Course' ) { search_course() }
else { get_name() }

print $query->end_html;

sub handicap_me {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Lets Go!!!!!'),
	$query->start_form;

  print $header;
  print $background;

  print $query->center(),
        $query->p("Welcome $user!, choose from the menu below"),
        $query->hidden( -name  => 'name',
		        -value => $user),
	$query->submit( -name  => 'State',
			-value => 'Enter New Score'),
        $query->submit( -name  => 'State',
		        -value => 'View Handicap'),
        $query->submit( -name  => 'State',
		        -value => 'Search by Score'),
        $query->submit( -name  => 'State',
		        -value => 'Search by Course'),
        $query->submit( -name  => 'State',
		        -value => 'Search by Date'),
        $query->submit( -name  => 'State',
		        -value => 'Log Out');

  print $footer;
}

sub enter_new {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Enter A New Score'),
        $query->start_form();
  print $header;
  print $background;
  print	$query->hidden( -name  => 'name',
			-value => $user),
        $query->center(),
        $query->p('Date You Played This Round:'),
	$query->p($query->textfield('date')),
	$query->p('Course Name'),
	$query->p($query->textfield('course')),
	$query->p('Par For This Course'),
	$query->p($query->textfield('par')),
	$query->p('Course Difficulty Rating'),
	$query->p($query->textfield('diff')),
	$query->p('Slope Rating'),
	$query->p($query->textfield('slope')),
	$query->p('Your Score'),
	$query->p($query->textfield('score')),
        $query->submit( -name=>'State',
                        -label=>'Submit Score'),
	$query->end_form;
  print $footer;

}

sub get_name {

  print $query->header(),
	$query->start_html('Welcome to Handicapper');

  print $header;
  print $background;

  print $query->start_form;

  print $query->center(), 
        $query->p('Please enter your username:'),
	$query->br($query->textfield('name')),
        $query->submit( -name=>'State',
                        -label=>'Lets Go!!!!!'),
	$query->end_form;
  print $footer;

}

sub search_score {
   
  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Search Database By Score'),
	$query->start_form();

  print $header;
  print $background;
  print $query->center(), 
        $query->p("This Screen will grep for users input and display back to screen"),
        $query->hidden( -name  => 'name',
		        -value => $user),
	$query->p('Please Enter Score To Search For'),
	$query->p($query->textfield('getscore')),
	$query->submit ( -name  => 'State',
			 -value => 'Show Scores'),
        $query->submit( -name  => 'State',
		        -value => 'Return To Main Menu');

  print $footer;
}

sub search_date {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Search Database By Date'),
	$query->start_form();

  print $header;
  print $background;
  print $query->center(), 
        $query->p("This Screen will grep for users input and display back to screen"),
        $query->hidden( -name  => 'name',
		        -value => $user),
	$query->p('Please Enter Date To Search For'),
	$query->p($query->textfield('getdate')),
	$query->submit ( -name  => 'State',
			 -value => 'Show Dates'),
        $query->submit( -name  => 'State',
		        -value => 'Return To Main Menu');

  print $footer;
}


sub search_course {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Search Database By Course'),
	$query->start_form();

  print $header;
  print $background;
  print $query->center(), 
        $query->p("This Screen will grep for users input and display back to screen"),
        $query->hidden( -name  => 'name',
		        -value => $user),
	$query->p('Please Enter Course To Search For'),
	$query->p($query->textfield('getcourse')),
	$query->submit ( -name  => 'State',
			 -value => 'Show Course'),
        $query->submit( -name  => 'State',
		        -value => 'Return To Main Menu');

  print $footer;
}

sub calc_score {

  $user = $query->param('name');
  $date = $query->param('date');
  $score = $query->param('score');
  $course = $query->param('course');
  $par = $query->param('par');
  $slope = $query->param('slope');
  $diff = $query->param('diff');
  
  open(DATAFILE, ">>$user.dat") || die "cannot append: $!";
  print DATAFILE "\n$date    |    $course    |    $score";
  close(DATAFILE);

  if ($score < 72) {
    $handicap = 0
    } else {

  $handicap = (($score - $par)* 113 / $slope);
  $handicap = $handicap - ((($score - $par)* 113 % $slope)/$slope);
   }

  open(INDEXFILE, ">>$user") || die "cannot append: $!";
  print INDEXFILE "\n$handicap";
  close(INDEXFILE);

  @hand = ("$user");

    foreach $hand (@hand) {
      $c = 0;
      $total = 0;
      $c = $c + 1;
      $total = $total + $hand;
  }
  $average = $total / $c;

  print $query->header(),

	$query->start_html('Display Handicap'),

  print $header;
  print $query->start_form;
  print $background;
  print $query->center(), 
        $query->p("Hey $user your handicap is $average!"),
        $query->hidden( -name  => 'name',
		        -value => $user),
        $query->submit( -name  => 'State',
		        -value => 'Enter Another Score'),
        $query->submit( -name  => 'State',
			-value => 'Return To Main Menu'),
        
	$query->end_form;
  print $footer;
}

sub view_handi {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('View Handicap'),
	$query->start_form();

  print $header;
  print $background;
  print $query->center(), 
        $query->p("$user, your current handicap is $average"),
        $query->hidden( -name  => 'name',
		        -value => $user),
        $query->submit( -name  => 'State',
		        -value => 'Return To Main Menu');

  print $footer;

}

sub show_scores {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Show Scores'),

  print $header;
  print $query->start_form;
  print $background;
  print $query->center(), 
        $query->p("List of Rounds by score for $user"),
        $query->hidden( -name  => 'name',
		        -value => $user),
        $query->submit( -name  => 'State',
		        -value => 'Search For Another Score'),
        $query->submit( -name  => 'State',
			-value => 'Return To Main Menu'),
        
	$query->end_form;
  print $footer;
}


sub show_dates {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Show Dates'),

  print $header;
  print $query->start_form;
  print $background;
  print $header;

  print $query->center(), 
        $query->p("List of Rounds by date for $user"),
        $query->hidden( -name  => 'name',
		        -value => $user),
        $query->submit( -name  => 'State',
		        -value => 'Search For Another Date'),
        $query->submit( -name  => 'State',
			-value => 'Return To Main Menu'),
        
	$query->end_form;
  print $footer;
  }

sub show_course {

  $user = $query->param('name');

  print $query->header(),
	$query->start_html('Show Course'),

  print $header;
  print $query->start_form;
  print $background;
  print $header;

  print $query->center(), 
        $query->p("List of Rounds by course for $user"),
        $query->hidden( -name  => 'name',
		        -value => $user),
        $query->submit( -name  => 'State',
		        -value => 'Search For Another Course'),
        $query->submit( -name  => 'State',
			-value => 'Return To Main Menu'),
        
	$query->end_form;
  print $footer;
  }

