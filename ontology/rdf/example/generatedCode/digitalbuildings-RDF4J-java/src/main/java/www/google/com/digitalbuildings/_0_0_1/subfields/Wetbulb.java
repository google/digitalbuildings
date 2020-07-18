package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Wetbulb 
* Describes air temperature measured at 100% relative humidity (saturation).
*/
@SuppressWarnings("serial")
public class Wetbulb extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IWetbulb{

	IRI newInstance;
	public Wetbulb(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wetbulb"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWetbulb> getAllWetbulbsObjectsCreated(){
		Set<IWetbulb> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wetbulb")).subjects().stream()
		.map(mapper->(IWetbulb)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}