package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.INo_analysis;
import www.google.com.digitalbuildings._0_0_1.No_analysis;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;

/**
* Class Ignore 
* Tag to ignore things. To be applied to devices which should not be onboarded.
*/
@SuppressWarnings("serial")
public class Ignore extends www.google.com.digitalbuildings._0_0_1.No_analysis implements IIgnore{

	IRI newInstance;
	public Ignore(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ignore"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IIgnore> getAllIgnoresObjectsCreated(){
		Set<IIgnore> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ignore")).subjects().stream()
		.map(mapper->(IIgnore)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}