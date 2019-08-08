<?php

	$aResult = array();
	$m = new MongoClient();
	$db = $m->myDatabase;
	$col = $db->matrix;
	$cursor = $col->find();
	$s="";
	foreach ($cursor as $document) {
      	$s = $s ." ". $document["DISEC"];
   	}
   	$aResult["result"] = $s;

    echo json_encode($aResult);

?>