package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;


@SuppressWarnings("serial")
public class Cdws implements ICdws{

	IRI newInstance;
	public Cdws(String namespace, String instanceId) {		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	@java.lang.Override
	public String stringValue() {
		return this.newInstance.getLocalName();
	}

	@java.lang.Override
	public String getNamespace() {
		return this.newInstance.getNamespace();
	}

	@java.lang.Override
	public String getLocalName() {
		return this.newInstance.getLocalName();
	}

	@java.lang.Override
	public String toString() {
		return this.newInstance.toString();
	}

	public static Set<ICdws> getAllCdwssObjectsCreated(){
		Set<ICdws> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws")).subjects().stream()
		.map(mapper->(ICdws)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}