package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;

/**
* Class Fan 
* Tag for stand-alone fans.
*/
@SuppressWarnings("serial")
public class Fan extends www.google.com.digitalbuildings._0_0_1.Equipment implements IFan{

	IRI newInstance;
	public Fan(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFan> getAllFansObjectsCreated(){
		Set<IFan> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan")).subjects().stream()
		.map(mapper->(IFan)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}